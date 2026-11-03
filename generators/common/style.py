"""SSOT hand-drawn style primitives. Shared by all generators."""
import random, os, sys, json, math

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
try:
    from .tokens import BG, INK, ACC, MID, CON, BDR, WHITE, FONT_UI
except ImportError:
    from tokens import BG, INK, ACC, MID, CON, BDR, WHITE, FONT_UI

ELEMENTS = []

def new():
    global ELEMENTS
    ELEMENTS = []
    return ELEMENTS

def _id():
    return f"{random.randint(100000000, 999999999)}"

def _base(t, x, y, w, h, stroke=INK, fill="transparent", sw=2, rough=1, fill_style="solid", dashed=False, angle=0):
    el = {
        "id": _id(), "type": t, "x": x, "y": y, "width": w, "height": h, "angle": angle,
        "strokeColor": stroke, "backgroundColor": fill, "fillStyle": fill_style,
        "strokeWidth": sw, "strokeStyle": "dashed" if dashed else "solid",
        "roughness": rough, "opacity": 100, "groupIds": [], "frameId": None,
        "roundness": None, "seed": random.randint(1, 2_000_000_000),
        "version": 1, "versionNonce": random.randint(1, 2_000_000_000),
        "isDeleted": False, "boundElements": [], "updated": 1700000000000,
        "link": None, "locked": False,
    }
    return el

def _push(el):
    ELEMENTS.append(el)
    return el

def rect(x, y, w, h, fill="transparent", stroke=INK, dash=False, rx=True, sw=4):
    el = _base("rectangle", x, y, w, h, stroke=stroke, fill=fill, sw=sw, rough=1, fill_style="hachure")
    el["roundness"] = {"type": 3} if rx else None
    el["strokeStyle"] = "dashed" if dash else "solid"
    return _push(el)

def ellipse(x, y, w, h, fill="transparent", stroke=INK, dash=False, sw=4):
    el = _base("ellipse", x, y, w, h, stroke=stroke, fill=fill, sw=sw, rough=1, fill_style="cross-hatch")
    el["strokeStyle"] = "dashed" if dash else "solid"
    return _push(el)

def line(x1, y1, x2, y2, color=INK, w=2, dash=False):
    el = _base("line", x1, y1, abs(x2-x1) or 1, abs(y2-y1) or 1, stroke=color, sw=w, rough=1, fill_style="hachure")
    el["points"] = [[0, 0], [x2 - x1, y2 - y1]]
    el["strokeStyle"] = "dashed" if dash else "solid"
    return _push(el)

def arrow(x1, y1, x2, y2, color=INK, w=4, dash=False, head="arrow", start=None, end=None):
    el = _base("arrow", x1, y1, abs(x2-x1) or 1, abs(y2-y1) or 1, stroke=color, sw=w, rough=1, fill_style="hachure")
    el["roundness"] = {"type": 2}
    el["points"] = [[0, 0], [x2 - x1, y2 - y1]]
    el["startArrowhead"] = None
    el["endArrowhead"] = head
    el["strokeStyle"] = "dashed" if dash else "solid"
    return _push(el)

def text(s, x, y, size=16, color=INK, align="left", anchor="lt", width=None, angle=0, font=FONT_UI):
    lines = s.split("\n")
    w = width if width else max(len(ln) for ln in lines) * size * 0.6 + 10
    h = len(lines) * size * 1.25
    ax, ay = x, y
    if anchor and anchor[0] == "c": ax = x - w/2
    elif anchor and anchor[0] == "r": ax = x - w
    if anchor and anchor[1] == "m": ay = y - h/2
    elif anchor and anchor[1] == "b": ay = y - h
    el = _base("text", ax, ay, w, h, stroke=color, fill="transparent", sw=1, rough=1, fill_style="solid", angle=angle)
    el.update({"text": s, "fontSize": size, "fontFamily": font, "textAlign": align,
               "verticalAlign": "top", "baseline": size, "containerId": None,
               "originalText": s, "lineHeight": 1.25, "roundness": None})
    return _push(el)

def freedraw(pts, stroke=INK, sw=3):
    if not pts: return None
    xs=[p[0] for p in pts]; ys=[p[1] for p in pts]
    minx,miny=min(xs),min(ys)
    w=max(max(xs)-minx,1); h=max(max(ys)-miny,1)
    rel=[[p[0]-minx,p[1]-miny] for p in pts]
    el=_base("freedraw", minx, miny, w, h, stroke=stroke, sw=sw, rough=0, fill_style="hachure")
    el["points"]=rel
    el["pressures"]=[]
    el["simulatePressure"]=True
    el["lastCommittedPoint"]=rel[-1]
    el["startBinding"]=None; el["endBinding"]=None
    el["startArrowhead"]=None; el["endArrowhead"]=None
    return _push(el)


def curved(x, y, pts, color=INK, w=4, dash=False, head="arrow", start=None):
    el = _base("arrow", x, y, abs(pts[-1][0]) or 1, abs(pts[-1][1]) or 1, stroke=color, sw=w, rough=2, fill_style="hachure")
    el["points"] = pts
    el["roundness"] = {"type": 2}
    el["startArrowhead"] = start
    el["endArrowhead"] = head
    el["strokeStyle"] = "dashed" if dash else "solid"
    return _push(el)
