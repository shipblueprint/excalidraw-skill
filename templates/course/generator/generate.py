#!/usr/bin/env python3
"""Generate starter Excalidraw scene for {{COURSE_NAME}}."""
import json
import os
import random
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))

OUT = os.path.join(HERE, "..", "generated")
os.makedirs(OUT, exist_ok=True)


def _nonce():
    return random.randint(1, 1000000)


def _id():
    return str(random.randint(100000000, 999999999))


def base(type_, x, y, **kw):
    el = {
        "type": type_, "version": 1, "versionNonce": _nonce(), "isDeleted": False,
        "id": _id(), "fillStyle": "solid", "strokeWidth": 2, "strokeStyle": "solid",
        "roughness": 0, "opacity": 100, "angle": 0, "x": x, "y": y,
        "strokeColor": "#1e1e1e", "backgroundColor": "transparent", "width": 0, "height": 0,
        "seed": _nonce(), "groupIds": [], "frameId": None, "roundness": None,
        "boundElements": None, "updated": int(time.time() * 1000), "link": None, "locked": False,
    }
    el.update(kw)
    return el


elements = []
elements.append(base("text", 100, 100, width=300, height=40, text="{{COURSE_NAME}}",
                    fontSize=32, fontFamily=1, textAlign="left", verticalAlign="top",
                    baseline=32, strokeColor="#1e1e1e"))

scene = {
    "type": "excalidraw",
    "version": 2,
    "source": "template",
    "elements": elements,
    "appState": {"viewBackgroundColor": "#ffffff"},
    "files": {},
}

path = os.path.join(OUT, "001 Starter.excalidraw")
with open(path, "w", encoding="utf-8") as f:
    json.dump(scene, f, indent=2, ensure_ascii=False)
print(f"Wrote {path}")
