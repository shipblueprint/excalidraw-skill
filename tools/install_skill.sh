#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DEST="$HOME/.config/opencode/skills/excalidraw-asset-pipeline"
mkdir -p "$DEST"
cp "$ROOT/SKILL.md" "$DEST/SKILL.md"
echo "Installed skill to $DEST"
