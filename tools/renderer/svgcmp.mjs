import { readFileSync } from 'fs';
import { exportToSvg } from '/home/lee/Downloads/extracted/tools/renderer/node_modules/@excalidraw/utils/dist/prod/index.js';
const files = [
  '/home/lee/Downloads/extracted/generators/hand-drawn/how_a_browser_works.excalidraw',
  '/home/lee/Downloads/extracted/generators/Building Agents That Never Sleep/generated/001 Welcome and What You\'ll Build.excalidraw',
];
for (const f of files) {
  const scene = JSON.parse(readFileSync(f,'utf8'));
  const svg = await exportToSvg({ elements: scene.elements, appState: scene.appState || {}, files: scene.files || {} });
  const str = typeof svg === 'string' ? svg : (svg.outerHTML || String(svg));
  const paths = (str.match(/<path/g)||[]).length;
  console.log(f.split('/').slice(-2).join('/'), 'svgChars=', str.length, 'paths=', paths);
}
