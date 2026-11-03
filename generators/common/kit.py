#!/usr/bin/env python3
"""
ekit — Excalidraw drawing kit for the Learn Software Architecture courses.

Palette (colors.md, light mode):
    BG  canvas background
    INK  primary lines + text
    ACC  accent / highlight (title, active component)
    MID  secondary text
    CON  container fill
    BDR  container border / dividers

Usage inside a scene script:

    from ekit import *
    new()
    title("Auto Scaling In The Cloud", 60, 40)
    box(60, 140, 200, 90, "Workload")
    server(360, 140, 120, 110, "Node")
    arrow(260, 185, 360, 185)
    save("Auto Scaling In The Cloud")

Every helper appends to a module-level element list; new() clears it.
"""
import json
import os
import random
import re
import time

OUT = None  # overridden by pack shim

import os as _os, sys as _sys
try:
    from .tokens import BG, INK, ACC, MID, CON, BDR, WHITE
except ImportError:
    from tokens import BG, INK, ACC, MID, CON, BDR, WHITE

_elements = []


# ---------------------------------------------------------------- internals
def _nonce():
    return random.randint(1, 1000000)


def _id():
    return str(random.randint(100000000, 999999999))


def base(type_, x, y, **kw):
    el = {
        "type": type_, "version": 1, "versionNonce": _nonce(), "isDeleted": False,
        "id": _id(), "fillStyle": "solid", "strokeWidth": 2, "strokeStyle": "solid",
        "roughness": 1, "opacity": 100, "angle": 0, "x": x, "y": y,
        "strokeColor": INK, "backgroundColor": "transparent", "width": 0, "height": 0,
        "seed": _nonce(), "groupIds": [], "frameId": None, "roundness": None,
        "boundElements": None, "updated": int(time.time() * 1000), "link": None, "locked": False,
    }
    el.update(kw)
    return el


def _push(el):
    _elements.append(el)
    return el


# ---------------------------------------------------------------- lifecycle
def new():
    _elements.clear()


def _is_watermark(el):
    # Drop only texts explicitly tagged by credit() (bare-domain credit lines).
    # A regex like `word.word` caused false hits on labels such as
    # "decision.action" — saving is now marker-based.
    return bool(el.get("watermark"))


def save(name, bg=None):
    scene = {
        "type": "excalidraw", "version": 2, "source": "https://excalidraw.com",
        "elements": [e for e in _elements if not _is_watermark(e)],
        "appState": {"gridSize": None, "viewBackgroundColor": bg if bg else "#ffffff"},
        "files": {},
    }
    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, name + ".excalidraw")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(scene, fh, ensure_ascii=False, indent=1)
    return path


# ---------------------------------------------------------------- primitives
def text(s, x, y, size=16, color=INK, align="left", anchor="lt", width=None, angle=0):
    lines = s.split("\n")
    w = width if width else max(len(ln) for ln in lines) * size * 0.60 + 10
    h = len(lines) * size * 1.25
    ax, ay = x, y
    if anchor[0] == "c":
        ax = x - w / 2
    elif anchor[0] == "r":
        ax = x - w
    if anchor[1] == "m":
        ay = y - h / 2
    elif anchor[1] == "b":
        ay = y - h
    return _push(base("text", ax, ay, width=w, height=h, text=s, fontSize=size, fontFamily=1,
                      textAlign=align, verticalAlign="top", baseline=size, containerId=None,
                      originalText=s, lineHeight=1.25, strokeColor=color, angle=angle))


def rect(x, y, w, h, fill="transparent", stroke=INK, dash=False, rx=True, sw=2):
    return _push(base("rectangle", x, y, width=w, height=h, backgroundColor=fill,
                      strokeColor=stroke, strokeWidth=sw, roundness={"type": 3} if rx else None,
                      strokeStyle="dashed" if dash else "solid"))


def ellipse(x, y, w, h, fill="transparent", stroke=INK, dash=False, sw=2):
    return _push(base("ellipse", x, y, width=w, height=h, backgroundColor=fill,
                      strokeColor=stroke, strokeWidth=sw,
                      strokeStyle="dashed" if dash else "solid"))


def line(x1, y1, x2, y2, color=INK, w=2, dash=False):
    return _push(base("line", x1, y1, points=[[0, 0], [x2 - x1, y2 - y1]], strokeColor=color,
                      strokeWidth=w, strokeStyle="dashed" if dash else "solid"))


def arrow(x1, y1, x2, y2, color=INK, w=2, dash=False, head="arrow", start=None):
    return _push(base("arrow", x1, y1, points=[[0, 0], [x2 - x1, y2 - y1]], strokeColor=color,
                      strokeWidth=w, strokeStyle="dashed" if dash else "solid",
                      startArrowhead=start, endArrowhead=head, roundness={"type": 2}))


def curved(x, y, pts, color=INK, w=2, dash=False, head="arrow", start=None):
    return _push(base("arrow", x, y, points=pts, strokeColor=color, strokeWidth=w,
                      strokeStyle="dashed" if dash else "solid", startArrowhead=start,
                      endArrowhead=head, roundness={"type": 2}))


def box(x, y, w, h, label, size=15, fill=CON, stroke=BDR, color=INK, rx=True, dash=False):
    rect(x, y, w, h, fill=fill, stroke=stroke, rx=rx, dash=dash)
    if label:
        text(label, x + w / 2, y + h / 2, size=size, align="center", anchor="cm", color=color)


def acc_box(x, y, w, h, label, size=15):
    """Highlighted box (accent border + tint)."""
    box(x, y, w, h, label, size=size, fill=WHITE, stroke=ACC, color=INK)


def title(s, x, y, size=24):
    text(s, x, y, size=size, color=INK)
    line(x, y + size * 1.5, x + max(120, len(s) * size * 0.5), y + size * 1.5, color=ACC, w=3)


def subtitle(s, x, y, size=14, width=None):
    return text(s, x, y, size=size, color=MID, width=width)


def credit(s="scaleyourapp.com", x=60, y=700):
    el = text(s, x, y, size=12, color=BDR)
    el["watermark"] = True
    return el


def dashed_group(x, y, w, h, label="", size=13):
    rect(x, y, w, h, fill="transparent", stroke=BDR, dash=True, rx=True, sw=2)
    if label:
        text(label, x + 10, y - 20, size=size, color=MID)


# ---------------------------------------------------------------- icons
def stick(cx, top, color=INK, scale=1.0):
    r = 10 * scale
    ellipse(cx - r, top, 2 * r, 2 * r, stroke=color)
    line(cx, top + 2 * r, cx, top + 5 * r, color=color)
    line(cx, top + 3 * r, cx - 1.5 * r, top + 4.5 * r, color=color)
    line(cx, top + 3 * r, cx + 1.5 * r, top + 4.5 * r, color=color)
    line(cx, top + 5 * r, cx - 1.5 * r, top + 7 * r, color=color)
    line(cx, top + 5 * r, cx + 1.5 * r, top + 7 * r, color=color)


def person(cx, top, label="", color=INK, scale=1.0, size=14):
    stick(cx, top, color, scale)
    if label:
        text(label, cx, top + 7 * 10 * scale + 6, size=size, align="center", anchor="ct", color=color)


def browser(x, y, w, h, label="", size=14, fill=WHITE, stroke=INK):
    rect(x, y, w, h, fill=fill, stroke=stroke, rx=True)
    line(x, y + 22, x + w, y + 22, color=stroke)
    for i in range(3):
        ellipse(x + 10 + i * 12, y + 7, 8, 8, stroke=stroke)
    if label:
        text(label, x + w / 2, y + 22 + (h - 22) / 2, size=size, align="center", anchor="cm", color=INK)


def mobile(x, y, w, h, label="", size=13, fill=WHITE, stroke=INK):
    rect(x, y, w, h, fill=fill, stroke=stroke, rx=True)
    line(x + w * 0.35, y + 10, x + w * 0.65, y + 10, color=stroke)
    if label:
        text(label, x + w / 2, y + h / 2, size=size, align="center", anchor="cm", width=w - 16, color=INK)


def server(x, y, w, h, label="", size=14, fill=CON, stroke=INK, color=INK):
    rect(x, y, w, h, fill=fill, stroke=stroke, rx=True)
    for i in (1, 2):
        line(x, y + h * i / 3, x + w, y + h * i / 3, color=stroke)
    for i in range(3):
        ellipse(x + 10 + i * 13, y + h * 0.16, 7, 7, fill=ACC, stroke=stroke)
    if label:
        text(label, x + w / 2, y + h * 0.62, size=size, align="center", anchor="cm", width=w - 12, color=color)


def database(x, y, w, h, label="", size=14, fill=CON, stroke=INK, color=INK):
    e = 26
    ellipse(x, y, w, e, fill=fill, stroke=stroke)
    ellipse(x, y + h - e, w, e, fill=fill, stroke=stroke)
    rect(x, y + e / 2, w, h - e, fill=fill, stroke=stroke, rx=False)
    if label:
        text(label, x + w / 2, y + h / 2 + 4, size=size, align="center", anchor="cm", width=w - 12, color=color)


def cache(x, y, w, h, label="", size=14, fill=WHITE, stroke=ACC, color=INK):
    rect(x, y, w, h, fill=fill, stroke=stroke, rx=True)
    line(x, y + h * 0.42, x + w, y + h * 0.42, color=stroke)
    line(x, y + h * 0.68, x + w, y + h * 0.68, color=stroke)
    if label:
        text(label, x + w / 2, y + h * 0.78, size=size, align="center", anchor="cm", width=w - 10, color=color)


def queue(x, y, w, h, label="", size=14, fill=CON, stroke=INK, color=INK):
    rect(x, y, w, h, fill=fill, stroke=stroke, rx=True)
    n = 4
    for i in range(n):
        bx = x + 10 + i * (w - 20) / n
        rect(bx, y + 12, (w - 20) / n * 0.7, h - 24, fill=WHITE, stroke=stroke, rx=True)
    if label:
        text(label, x + w / 2, y + h + 6, size=size, align="center", anchor="ct", color=color)


def cloud(cx, cy, w=180, h=100, label="", size=15, fill=CON, stroke=INK, color=INK):
    r = h * 0.42
    ellipse(cx - w * 0.28, cy - r * 0.4, r * 1.6, r * 1.6, fill=fill, stroke=stroke)
    ellipse(cx - r * 0.2, cy - r * 0.9, r * 1.9, r * 1.9, fill=fill, stroke=stroke)
    ellipse(cx + w * 0.2, cy - r * 0.4, r * 1.5, r * 1.5, fill=fill, stroke=stroke)
    rect(cx - w * 0.45, cy + r * 0.1, w * 0.9, r * 0.8, fill=fill, stroke=stroke, rx=True)
    if label:
        text(label, cx, cy + r * 1.6, size=size, align="center", anchor="ct", color=color)


def hexagon(x, y, w, h, label="", size=14, fill=CON, stroke=INK, color=INK):
    pts = [[w * 0.25, 0], [w * 0.75, 0], [w, h / 2], [w * 0.75, h], [w * 0.25, h], [0, h / 2]]
    _push(base("line", x, y, points=pts, strokeColor=stroke, backgroundColor=fill, strokeWidth=2))
    if label:
        text(label, x + w / 2, y + h / 2, size=size, align="center", anchor="cm", color=color)


def container(x, y, w, h, label="", size=13, fill=CON, stroke=INK, color=INK):
    rect(x, y, w, h, fill=fill, stroke=stroke, rx=True)
    for i in (1, 2, 3):
        line(x, y + h * i / 4, x + w, y + h * i / 4, color=stroke)
    if label:
        text(label, x + w / 2, y + h + 6, size=size, align="center", anchor="ct", color=color)


def vm(x, y, w, h, label="", size=13, fill=WHITE, stroke=INK, color=INK):
    rect(x, y, w, h, fill=fill, stroke=stroke, rx=True)
    rect(x + 10, y + 10, w - 20, h - 20, fill="transparent", stroke=stroke, rx=True)
    if label:
        text(label, x + w / 2, y + h / 2, size=size, align="center", anchor="cm", width=w - 24, color=color)


def dns(x, y, w, h, label="", size=13, fill=WHITE, stroke=INK, color=INK):
    ellipse(x, y, w, h, fill=fill, stroke=stroke)
    ellipse(x + w * 0.35, y, w * 0.3, h, stroke=stroke)
    line(x, y + h / 2, x + w, y + h / 2, color=stroke)
    if label:
        text(label, x + w / 2, y + h + 6, size=size, align="center", anchor="ct", color=color)


def storage(x, y, w, h, label="", size=13, fill=CON, stroke=INK, color=INK):
    n = 3
    for i in range(n):
        yy = y + i * h / (n + 1)
        rect(x, yy, w, h / (n + 1), fill=fill, stroke=stroke, rx=True)
    if label:
        text(label, x + w / 2, y + h * 0.75, size=size, align="center", anchor="cm", color=color)


def document(x, y, w, h, label="", size=13, fill=WHITE, stroke=INK, color=INK):
    rect(x, y, w, h, fill=fill, stroke=stroke, rx=True)
    line(x + w * 0.65, y, x + w * 0.65, y + h * 0.3, color=stroke)
    line(x + w * 0.65, y + h * 0.3, x + w, y + h * 0.3, color=stroke)
    if label:
        text(label, x + w / 2, y + h * 0.6, size=size, align="center", anchor="cm", width=w - 10, color=color)


def firewall(x, y, w, h, label="", size=13, fill=CON, stroke=INK, color=INK):
    rect(x, y, w, h, fill=fill, stroke=stroke, rx=False)
    rows = 4
    for i in range(1, rows):
        line(x, y + h * i / rows, x + w, y + h * i / rows, color=stroke)
        off = 0 if i % 2 else w / 6
        for j in range(1, 4):
            line(x + w * j / 4 + off if off else x + w * j / 4, y + h * (i - 1) / rows,
                 x + w * j / 4 + off if off else x + w * j / 4, y + h * i / rows, color=stroke)
    if label:
        text(label, x + w / 2, y + h + 6, size=size, align="center", anchor="ct", color=color)


def gear(cx, cy, r=26, color=INK, teeth=8):
    ellipse(cx - r, cy - r, 2 * r, 2 * r, stroke=color)
    import math
    for i in range(teeth):
        a = i * 2 * math.pi / teeth
        x1, y1 = cx + math.cos(a) * r, cy + math.sin(a) * r
        x2, y2 = cx + math.cos(a) * (r + 10), cy + math.sin(a) * (r + 10)
        line(x1, y1, x2, y2, color=color)


def badge(cx, cy, n, r=15, fill=ACC, color=WHITE, size=15):
    ellipse(cx - r, cy - r, 2 * r, 2 * r, fill=fill, stroke=fill)
    text(str(n), cx, cy, size=size, align="center", anchor="cm", color=color)


# ---------------------------------------------------------------- arrows helpers
def arrow_right(x, y, length=70, label="", color=INK, dash=False):
    arrow(x, y, x + length, y, color=color, dash=dash)
    if label:
        text(label, x + length / 2, y - 8, size=11, color=MID, align="center", anchor="cb")


def arrow_down(x, y, length=70, label="", color=INK, dash=False):
    arrow(x, y, x, y + length, color=color, dash=dash)
    if label:
        text(label, x + 6, y + length / 2, size=11, color=MID, align="left", anchor="lm")


def arrow_bidir(x1, y1, x2, y2, color=INK, dash=False):
    arrow(x1, y1, x2, y2, color=color, dash=dash, start="arrow")
