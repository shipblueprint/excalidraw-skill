// Render .excalidraw scenes to PNG with Excalidraw's own rendering engine.
// Unified light + dark renderer. By default renders BOTH modes:
//   <folder>/png/       (light)
//   <folder>/png-dark/  (dark, brand dark palette)
// MODE=light|dark|both controls which modes run.
// DARK=1 is a legacy alias for MODE=dark.
// SCALE=3 sets export scale (default 2).
import { JSDOM } from 'jsdom';
import { readFileSync, writeFileSync, readdirSync, mkdirSync, statSync, rmSync } from 'fs';
import path from 'path';
import { Resvg } from '@resvg/resvg-js';

const dom = new JSDOM('<!doctype html><html><body></body></html>', {
  pretendToBeVisual: true,
  url: 'http://localhost/',
});
globalThis.window = dom.window;
globalThis.document = dom.window.document;
Object.defineProperty(globalThis, 'navigator', { value: dom.window.navigator, configurable: true });
Object.defineProperty(globalThis, 'devicePixelRatio', { value: 2, configurable: true });
Object.defineProperty(globalThis, 'screen', { value: dom.window.screen, configurable: true });
Object.defineProperty(globalThis, 'localStorage', { value: dom.window.localStorage, configurable: true });
if (!globalThis.matchMedia) {
  globalThis.matchMedia = () => ({
    matches: false,
    addListener() {}, removeListener() {},
    addEventListener() {}, removeEventListener() {},
  });
}
const { exportToSvg } = await import('@excalidraw/utils');

const folder = process.argv[2];
if (!folder) {
  console.error('usage: node render_all.mjs <folder-with-.excalidraw-files> [scene-basename]\n' +
    'MODE=light|dark|both (default both)\n' +
    'DARK=1 -> dark only (legacy)\n' +
    'SCALE=3 -> non-default scale (default 2)');
  process.exit(1);
}
const only = process.argv[3] || null;
const SCALE = Number(process.env.SCALE || 2);

let mode = process.env.MODE;
if (!mode && process.env.DARK === '1') mode = 'dark';
if (!mode) mode = 'both';
const modes = mode === 'both' ? ['light', 'dark'] : [mode];

// Brand tokens (single source of truth).
const tokens = JSON.parse(readFileSync(path.join(path.dirname(new URL(import.meta.url).pathname), '..', '..', 'generators', 'common', 'tokens.json'), 'utf8'));
const LIGHT = tokens.light;
const DARKT = tokens.dark;
const DARK_PALETTE = {};
for (const key of Object.keys(LIGHT)) {
  DARK_PALETTE[LIGHT[key]] = DARKT[key];
  DARK_PALETTE[LIGHT[key].toLowerCase()] = DARKT[key];
  DARK_PALETTE[LIGHT[key].toUpperCase()] = DARKT[key];
}
// Legacy aliases not represented as distinct brand tokens.
Object.assign(DARK_PALETTE, {
  [LIGHT.ink]: DARKT.ink,
  [LIGHT.mid]: DARKT.mid,
  [LIGHT.border]: DARKT.border,
  [LIGHT.accent]: DARKT.accent,
  [LIGHT.container]: DARKT.container,
  [LIGHT.bg]: DARKT.bg,
  [tokens.semantic.black]: DARKT.ink,
  [tokens.semantic.gray]: DARKT.mid,
  [tokens.semantic.borderLight]: DARKT.mid,
  [tokens.semantic.lightBorderAlt]: DARKT.border,
  [tokens.semantic.inkDark]: DARKT.mid,
  [tokens.semantic.white]: DARKT.container,
  'white': DARKT.container,
});
const swap = (c) => (typeof c === 'string' ? (DARK_PALETTE[c] || c) : c);
const toDarkElements = (elements) => elements.map((el) => {
  const e = { ...el };
  if (typeof e.strokeColor === 'string') e.strokeColor = swap(e.strokeColor);
  if (typeof e.backgroundColor === 'string') e.backgroundColor = swap(e.backgroundColor);
  return e;
});

const scanDirs = [folder, path.join(folder, 'excalidraw')];
let files = [];
for (const dir of scanDirs) {
  try {
    files.push(...readdirSync(dir).filter((f) => f.endsWith('.excalidraw')).map((f) => path.join(dir, f)));
  } catch {}
}
if (!files.length) {
  console.error(`no .excalidraw files found in ${folder} (or ${folder}/excalidraw)`);
  process.exit(1);
}
if (only) files = files.filter((p) => path.basename(p) === only || path.basename(p, '.excalidraw') === only);

for (const currentMode of modes) {
  const dark = currentMode === 'dark';
  const out = path.join(folder, dark ? 'png-dark' : 'png');
  mkdirSync(out, { recursive: true });
  let ok = 0;
  const fail = [];
  for (const src of files) {
    const png = path.join(out, path.basename(src).replace(/\.excalidraw$/, '.png'));
    try {
      if (statSync(png).mtimeMs >= statSync(src).mtimeMs) { ok++; continue; }
    } catch {}
    try {
      const scene = JSON.parse(readFileSync(src, 'utf8'));
      const svg = await exportToSvg({
        data: {
          elements: dark ? toDarkElements(scene.elements) : scene.elements,
          appState: {
            viewBackgroundColor: dark ? DARKT.bg : (scene.appState && scene.appState.viewBackgroundColor) || LIGHT.bg,
            exportBackground: true,
            exportWithDarkMode: false,
            exportPadding: 10,
            exportScale: SCALE,
          },
          files: {},
        },
        config: { skipInliningFonts: true },
      });
      const resvg = new Resvg(svg.outerHTML, { fitTo: { mode: 'original' } });
      const pngData = resvg.render();
      writeFileSync(png, pngData.asPng());
      ok++;
      if (!pngData.width || !pngData.height) {
        fail.push([folder, path.basename(src), 'empty render (' + pngData.width + 'x' + pngData.height + ')']);
        rmSync(png, { force: true });
      }
    } catch (e) {
      fail.push([folder, path.basename(src), String((e && e.message) || e).slice(0, 160)]);
      try { rmSync(png, { force: true }); } catch {}
    }
  }
  console.log(`[${dark ? 'dark ' : 'light'}] ${files.length} scene(s) in ${folder} -> ${out}: ${ok} ok; failures ${fail.length}`);
  for (const x of fail) console.log('FAIL | ' + x.join(' | '));
}
