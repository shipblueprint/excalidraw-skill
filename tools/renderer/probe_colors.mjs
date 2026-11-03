// Probe: what does exportToSvg produce in light vs dark (background + which fill/stroke values)?
import { JSDOM } from 'jsdom';
import { readFileSync } from 'fs';

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
  globalThis.matchMedia = () => ({ matches: false, addListener() {}, removeListener() {}, addEventListener() {}, removeEventListener() {} });
}
const { exportToSvg } = await import('@excalidraw/utils');

const src = process.argv[process.argv.indexOf('--palette') >= 0 ? process.argv.length - 1 : 2];
const PALETTE_PATH = process.argv.includes('--palette');
const scene = JSON.parse(readFileSync(src, 'utf8'));
console.log('VIEW_BG =', JSON.stringify(scene.appState && scene.appState.viewBackgroundColor));

// mirrors the DARK_PALETTE map in render_all.mjs
const _tokens = JSON.parse(readFileSync(new URL('../../generators/common/tokens.json', import.meta.url)));
const _LIGHT = _tokens.light; const _DARKT = _tokens.dark;
const DARK_PALETTE = {};
for (const k of Object.keys(_LIGHT)) DARK_PALETTE[_LIGHT[k]] = _DARKT[k];
Object.assign(DARK_PALETTE, { [_tokens.semantic.black]: _DARKT.ink, [_tokens.semantic.gray]: _DARKT.mid, [_tokens.semantic.borderLight]: _DARKT.mid, [_tokens.semantic.lightBorderAlt]: _DARKT.border, [_tokens.semantic.inkDark]: _DARKT.mid, [_tokens.semantic.white]: _DARKT.container, 'white': _DARKT.container });
const swap = (c) => DARK_PALETTE[c] || c;

for (const DARK of [false, PALETTE_PATH]) {
  const elements = PALETTE_PATH ? scene.elements.map((el) => ({ ...el, strokeColor: swap(el.strokeColor), backgroundColor: swap(el.backgroundColor) })) : scene.elements;
  const svg = await exportToSvg({
    data: {
      elements,
      appState: {
        viewBackgroundColor: PALETTE_PATH ? _DARKT.bg : (scene.appState && scene.appState.viewBackgroundColor) || _LIGHT.bg,
        exportBackground: true,
        exportWithDarkMode: false,
        exportPadding: 10,
        exportScale: 2,
      },
      files: {},
    },
    config: { skipInliningFonts: true },
  });
  const s = svg.outerHTML;
  const mode = PALETTE_PATH ? 'DARK-PALETTE' : 'LIGHT';
  const bg = (s.match(/<rect x="0" y="0"[^>]*fill="([^"]*)"/) || [])[1] || '(none)';
  const fills = new Set([...s.matchAll(/fill="(#\w+)"/g)].map(m => m[1]));
  const strokes = new Set([...s.matchAll(/stroke="(#\w+)"/g)].map(m => m[1]));
  console.log(`\n== ${mode} ==`);
  console.log('BG rect fill =', bg);
  console.log('fill values  =', [...fills].sort().join(' '));
  console.log('stroke values=', [...strokes].sort().join(' '));
}