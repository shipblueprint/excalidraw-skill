#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../../../.." && pwd)"
SRC="$ROOT/.opencode/skills/excalidraw-asset-pipeline"
DEST="$HOME/.config/opencode/skills/excalidraw-asset-pipeline"
mkdir -p "$HOME/.config/opencode/skills"
rm -rf "$DEST"
ln -s "$SRC" "$DEST"
echo "Installed skill symlink: $DEST -> $SRC"
