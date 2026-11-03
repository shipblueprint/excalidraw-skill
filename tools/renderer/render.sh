#!/usr/bin/env bash
# Render .excalidraw scenes to PNG (light + dark) with Excalidraw's own engine.
# Nothing is hardcoded — pass the folder that holds the .excalidraw files:
#
#   bash render.sh <folder> [scene-basename]
#
#   bash render.sh "/…/building-agents-that-never-sleep/excalidraw"           # light + dark -> <folder>/png/ + png-dark/
#   bash render.sh "/…/cloud-computing-101-master-the-fundamentals/excalidraw"
#   bash render.sh "<folder>" "Figure 1.10"                                   # one scene
#   SCALE=3 bash render.sh "<folder>"                                         # non-default scale (2 default)
#
# Output is always created next to the input:
#   <folder>/png/       light (2x, scene bg) — copy these into the course's images/
#   <folder>/png-dark/  dark — Field Notebook palette (#171513 canvas, see _handoff/colors.md)
set -euo pipefail
cd "$(dirname "$0")"

if [ $# -lt 1 ]; then
  echo "usage: bash render.sh <folder-with-.excalidraw-files> [scene-basename]
  bash render.sh \"/…/My Course/excalidraw\"                 both modes
  bash render.sh \"<folder>\" \"Figure 1.10\"                  one scene
  SCALE=3 bash render.sh \"<folder>\"                         non-default scale" >&2
  exit 1
fi

[ -d node_modules ] || npm install

echo "== light mode =="
node render_all.mjs "$@"
echo "== dark mode =="
DARK=1 node render_all.mjs "$@"