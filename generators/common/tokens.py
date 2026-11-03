"""Brand tokens (SSOT) — sourced from brand-webapps light theme."""
import json
import os

_TOKENS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tokens.json")
with open(_TOKENS_PATH, encoding="utf-8") as f:
    TOKENS = json.load(f)

LIGHT = TOKENS["light"]
DARK = TOKENS["dark"]
SEMANTIC = TOKENS["semantic"]
FONT = TOKENS.get("font", {})

BG = LIGHT["bg"]
INK = LIGHT["ink"]
ACC = LIGHT["accent"]
MID = LIGHT["mid"]
CON = LIGHT["container"]
BDR = LIGHT["border"]
WHITE = LIGHT["surface"]

# Excalidraw built-in font family closest to brand UI font (Inter).
FONT_UI = 1
FONT_DISPLAY = 1
