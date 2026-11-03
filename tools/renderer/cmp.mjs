import { readFileSync } from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { JSDOM } from 'jsdom';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, '..', '..');

const _dom = new JSDOM('<!doctype html><html><body></body></html>', { pretendToBeVisual: true, url: 'http://localhost/' });
globalThis.window = _dom.window;
globalThis.document = _dom.window.document;
Object.defineProperty(globalThis, 'navigator', { value: _dom.window.navigator, configurable: true });
Object.defineProperty(globalThis, 'devicePixelRatio', { value: 2, configurable: true });

const { exportToSvg } = await import('./node_modules/@excalidraw/utils/dist/prod/index.js');

const files = [
  path.join(ROOT, 'generators', 'hand-drawn', 'how_a_browser_works.excalidraw'),
  path.join(ROOT, 'generators', 'building-agents-that-never-sleep', 'generated', '001 Welcome and What You\'ll Build.excalidraw'),
];
for (const f of files) {
  const scene = JSON.parse(readFileSync(f, 'utf8'));
  const svg = await exportToSvg({ data: { elements: scene.elements, appState: scene.appState || {}, files: scene.files || {} }, config: { skipInliningFonts: true } });
  const str = typeof svg === 'string' ? svg : svg.outerHTML;
  const paths = (str.match(/<path/g) || []).length;
  const curves = (str.match(/[CcQq]/g) || []).length;
  console.log(path.basename(f), 'paths=', paths, 'curves=', curves, 'svgChars=', str.length);
}
