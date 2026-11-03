"""
how_a_browser_works.excalidraw, hand-drawn Excalidraw
roughness=2 + Virgil + cross-hatch + freedraw accents
"""
import json, random, math
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from common.tokens import BG, INK, ACC, MID, CON, BDR, WHITE, SEMANTIC, FONT_UI


class HandDrawn:
    def __init__(self, seed=21):
        self.elements, self._c, self._rng = [], 1000, random.Random(seed)

    def _id(self):
        self._c += 1
        return f"{self._c:016x}"

    def _seed(self):
        return self._rng.randint(1, 2_000_000_000)

    def _base(self, t, x, y, w, h, stroke=INK, fill="transparent",
              sw=4, rough=2, fill_style="cross-hatch", dashed=False):
        return {
            "id": self._id(), "type": t, "x": x, "y": y,
            "width": w, "height": h, "angle": 0,
            "strokeColor": stroke, "backgroundColor": fill,
            "fillStyle": fill_style, "strokeWidth": sw,
            "strokeStyle": "dashed" if dashed else "solid",
            "roughness": rough, "opacity": 100,
            "groupIds": [], "frameId": None, "roundness": None,
            "seed": self._seed(), "version": 1,
            "versionNonce": self._seed(), "isDeleted": False,
            "boundElements": [], "updated": 1700000000000,
            "link": None, "locked": False,
        }

    # ---- rectangle: pill + slight rotation + cross-hatch fill ----
    def rect(self, x, y, w, h, fill, stroke, sw=4, rough=2):
        r = self._base("rectangle", x, y, w, h,
                       stroke=stroke, fill=fill, sw=sw, rough=rough,
                       fill_style="cross-hatch")
        r["angle"] = self._rng.uniform(-0.018, 0.018)   # hand-tilt
        r["roundness"] = {"type": 3}
        self.elements.append(r)
        return r["id"]

    # ---- text bound to a box (Virgil font = 1) ----
    def text_in(self, box_id, text, size=18, color=INK, font=FONT_UI):
        box = next(e for e in self.elements if e["id"] == box_id)
        lines = text.split("\n")
        lh = size * 1.25
        th = lh * len(lines)
        tw = max(len(l) for l in lines) * size * 0.55
        t = self._base("text",
                       box["x"] + (box["width"] - tw) / 2,
                       box["y"] + (box["height"] - th) / 2,
                       tw, th, color, "transparent", 1, 0,
                       fill_style="hachure")
        t.update({
            "text": text, "fontSize": size, "fontFamily": font,
            "textAlign": "center", "verticalAlign": "middle",
            "baseline": int(size * 0.9),
            "containerId": box_id, "originalText": text,
            "lineHeight": 1.25, "roundness": None,
        })
        box["boundElements"].append({"id": t["id"], "type": "text"})
        self.elements.append(t)
        return t["id"]

    def text(self, x, y, text, size=20, color=INK, font=FONT_UI, align="left"):
        lines = text.split("\n")
        lh = size * 1.25
        th = lh * len(lines)
        tw = max(len(l) for l in lines) * size * 0.55
        t = self._base("text", x, y, tw, th, color, "transparent", 1, 0,
                       fill_style="hachure")
        t.update({
            "text": text, "fontSize": size, "fontFamily": font,
            "textAlign": align, "verticalAlign": "top",
            "baseline": int(size * 0.9),
            "containerId": None, "originalText": text,
            "lineHeight": 1.25, "roundness": None,
        })
        self.elements.append(t)
        return t["id"]

    # ---- arrow bound to two boxes ----
    def arrow(self, x1, y1, x2, y2, stroke=INK, sw=4,
              start_id=None, end_id=None, gap=4):
        aid = self._id()
        a = self._base("arrow", x1, y1, abs(x2-x1) or 1, abs(y2-y1) or 1,
                       stroke=stroke, sw=sw, rough=2,
                       fill_style="hachure")
        a["roundness"] = {"type": 2}
        a["points"] = [[0, 0], [x2 - x1, y2 - y1]]
        a["lastCommittedPoint"] = None
        a["startBinding"] = ({"elementId": start_id, "focus": 0,
                              "gap": gap} if start_id else None)
        a["endBinding"]   = ({"elementId": end_id, "focus": 0,
                              "gap": gap} if end_id else None)
        a["startArrowhead"] = None
        a["endArrowhead"] = "arrow"
        self.elements.append(a)
        for bid in (start_id, end_id):
            if not bid: continue
            el = next(e for e in self.elements if e["id"] == bid)
            el["boundElements"].append({"id": aid, "type": "arrow"})
        return aid

    # ---- freedraw: actual hand-traced path (most "alive") ----
    def freedraw(self, abs_pts, stroke=INK, sw=3):
        if not abs_pts: return None
        xs = [p[0] for p in abs_pts]; ys = [p[1] for p in abs_pts]
        min_x, min_y = min(xs), min(ys)
        w = max(max(xs) - min_x, 1); h = max(max(ys) - min_y, 1)
        rel = [[p[0] - min_x, p[1] - min_y] for p in abs_pts]
        f = self._base("freedraw", min_x, min_y, w, h,
                       stroke=stroke, sw=sw, rough=0,
                       fill_style="hachure")
        f["points"] = rel
        f["pressures"] = []
        f["simulatePressure"] = True
        f["lastCommittedPoint"] = rel[-1]
        f["startBinding"] = f["endBinding"] = None
        f["startArrowhead"] = f["endArrowhead"] = None
        self.elements.append(f)
        return f["id"]

    # ---- wavy freedraw line helper (for underline / timeline) ----
    def wavy(self, x1, y1, x2, y2, stroke, sw=2, segments=40, amp=2.5):
        pts = []
        for i in range(segments + 1):
            t = i / segments
            x = x1 + (x2 - x1) * t
            y = y1 + (y2 - y1) * t + math.sin(t * 12) * amp \
                + self._rng.uniform(-0.6, 0.6)
            pts.append([x, y])
        return self.freedraw(pts, stroke=stroke, sw=sw)

    def save(self, path):
        with open(path, "w", encoding="utf-8") as f:
            json.dump({
                "type": "excalidraw", "version": 2,
                "source": "https://excalidraw.com",
                "elements": self.elements,
                "appState": {"gridSize": None,
                             "viewBackgroundColor": BG},
                "files": {},
            }, f, indent=2, ensure_ascii=False)


def build(path="how_a_browser_works.excalidraw"):
    b = HandDrawn(seed=21)
    RT_Y, RT_H = 180, 130
    NW_Y, NW_H = 470, 90
    TL_Y = 700

    # Title (Virgil = 1)
    b.text(420, 30, "How a Browser Works", size=52, font=FONT_UI, align="center")
    # Hand-drawn wavy underline (freedraw)
    b.wavy(440, 100, 880, 100, stroke=SEMANTIC["accentBlue"], sw=3, segments=70, amp=4)

    # Lane labels
    b.text(40, RT_Y + 35, "Runtime", size=34, color=SEMANTIC["purple"], font=FONT_UI)
    b.text(40, NW_Y + 25, "Network", size=34, color=ACC, font=FONT_UI)

    # Runtime boxes — every box gets a UNIQUE seed → unique rough path
    rt = [
        b.rect(160,  RT_Y, 170, RT_H, SEMANTIC["lightPurple"], SEMANTIC["purple"]),
        b.rect(360,  RT_Y, 260, RT_H, SEMANTIC["lightAccentBlue"], SEMANTIC["accentBlue"]),
        b.rect(660,  RT_Y, 200, RT_H, SEMANTIC["lightGreen"], SEMANTIC["green"]),
        b.rect(900,  RT_Y, 280, RT_H, SEMANTIC["yellow"], SEMANTIC["orange"]),
        b.rect(1220, RT_Y, 180, RT_H, SEMANTIC["lightRed"], SEMANTIC["red"]),
    ]
    b.text_in(rt[0], "Navigate\nto page", size=22)
    b.text_in(rt[1], "Start parsing HTML\n(during download)\n— Parse HTML", size=16)
    b.text_in(rt[2], "Calculate styles\n— Parse CSS", size=16)
    b.text_in(rt[3], "Apply elements & styles\nto window size\n— Layout   — Paint", size=16)
    b.text_in(rt[4], "The view\nupdates", size=22)

    # Horizontal flow arrows (bound + rough)
    for i in range(4):
        p = next(e for e in b.elements if e["id"] == rt[i])
        n = next(e for e in b.elements if e["id"] == rt[i+1])
        b.arrow(p["x"] + p["width"], p["y"] + p["height"]/2,
                n["x"],              n["y"] + n["height"]/2,
                stroke=INK, sw=4,
                start_id=rt[i], end_id=rt[i+1])

    # Network boxes
    n1 = b.rect(400, NW_Y, 180, NW_H, SEMANTIC["lightOrange"], ACC)
    n2 = b.rect(680, NW_Y, 180, NW_H, SEMANTIC["lightOrange"], ACC)
    b.text_in(n1, "Get HTML", size=22)
    b.text_in(n2, "Get CSS",  size=22)

    # Vertical arrows Network → Runtime
    n1e = next(e for e in b.elements if e["id"] == n1)
    n2e = next(e for e in b.elements if e["id"] == n2)
    b2e = next(e for e in b.elements if e["id"] == rt[1])
    b3e = next(e for e in b.elements if e["id"] == rt[2])
    b.arrow(n1e["x"] + n1e["width"]/2, n1e["y"],
            b2e["x"] + b2e["width"]/2, b2e["y"] + b2e["height"],
            stroke=ACC, sw=4, start_id=n1, end_id=rt[1])
    b.arrow(n2e["x"] + n2e["width"]/2, n2e["y"],
            b3e["x"] + b3e["width"]/2, b3e["y"] + b3e["height"],
            stroke=ACC, sw=4, start_id=n2, end_id=rt[2])

    # Hand-drawn timeline (freedraw wavy baseline)
    b.wavy(160, TL_Y, 1400, TL_Y, stroke=MID, sw=2,
           segments=200, amp=1.8)
    for x, label in [(160, "navigate"), (360, "parse HTML"),
                     (660, "parse CSS"), (900, "layout"),
                     (1180, "paint"), (1400, "view")]:
        # Hand-drawn tick (freedraw vertical squiggle)
        tick = [[x + b._rng.uniform(-1, 1),
                 TL_Y - 10 + j * 2 + b._rng.uniform(-0.5, 0.5)]
                for j in range(11)]
        b.freedraw(tick, stroke=MID, sw=2)
        b.text(x - 45, TL_Y + 18, label, size=15,
               color=MID, font=FONT_UI, align="center")

    b.save(path)
    print(f"✓ {path}  ({len(b.elements)} elements)")


if __name__ == "__main__":
    build()