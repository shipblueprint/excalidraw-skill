#!/usr/bin/env python3
"""
Generate Excalidraw recreations of every content image in the
'Software Developers Roadmap to Excellence' course.

Same approach as the reference excalidraw-example/excal.py: build the elements
programmatically and dump an .excalidraw scene.  Run:

    python3 generate.py

Outputs one <image-name>.excalidraw per source image into this folder.
"""
import json
import os
import random
import re
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from common.tokens import SEMANTIC, FONT_UI

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "generated")
os.makedirs(OUT, exist_ok=True)

INK = SEMANTIC["inkDark"]
SUBTLE = SEMANTIC["subtle"]
BLUE, BLUE_F = SEMANTIC["accentBlue"], SEMANTIC["fillBlue"]
GREEN, GREEN_F = SEMANTIC["green"], SEMANTIC["fillGreen"]
ORANGE, ORANGE_F = SEMANTIC["darkOrange"], SEMANTIC["fillOrange"]
RED, RED_F = SEMANTIC["red"], SEMANTIC["fillRed"]
PURPLE, PURPLE_F = SEMANTIC["violet"], SEMANTIC["lightViolet"]
GRAY, GRAY_F = SEMANTIC["gray"], SEMANTIC["lightGray"]
YELLOW, YELLOW_F = SEMANTIC["orange"], SEMANTIC["lightYellow"]
TEAL, TEAL_F = SEMANTIC["teal"], SEMANTIC["lightTeal"]

_elements = []


def _nonce():
    return random.randint(1, 1000000)


def _id():
    return str(random.randint(100000000, 999999999))


def base(type_, x, y, **kw):
    el = {
        "type": type_, "version": 1, "versionNonce": _nonce(), "isDeleted": False,
        "id": _id(), "fillStyle": "hachure", "strokeWidth": 2, "strokeStyle": "solid",
        "roughness": 1, "opacity": 100, "angle": 0, "x": x, "y": y,
        "strokeColor": INK, "backgroundColor": "transparent", "width": 0, "height": 0,
        "seed": _nonce(), "groupIds": [], "frameId": None, "roundness": None,
        "boundElements": None, "updated": int(time.time() * 1000), "link": None, "locked": False,
    }
    el.update(kw)
    return el


# ---------------------------------------------------------------- primitives
def text(s, x, y, size=18, color=INK, align="left", anchor="lt", width=None, angle=0):
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
    el = base("text", ax, ay, width=w, height=h, text=s, fontSize=size, fontFamily=FONT_UI,
              textAlign=align, verticalAlign="top", baseline=size, containerId=None,
              originalText=s, lineHeight=1.25, strokeColor=color, angle=angle)
    _elements.append(el)
    return el


def rect(x, y, w, h, fill="transparent", stroke=INK, dash=False, rx=True):
    el = base("rectangle", x, y, width=w, height=h, backgroundColor=fill,
              strokeColor=stroke, roundness={"type": 3} if rx else None,
              strokeStyle="dashed" if dash else "solid")
    _elements.append(el)
    return el


def ellipse(x, y, w, h, fill="transparent", stroke=INK, dash=False):
    el = base("ellipse", x, y, width=w, height=h, backgroundColor=fill,
              strokeColor=stroke, strokeStyle="dashed" if dash else "solid")
    _elements.append(el)
    return el


def arrow(x1, y1, x2, y2, color=INK, w=2, dash=False, head="arrow", start=None):
    el = base("arrow", x1, y1, points=[[0, 0], [x2 - x1, y2 - y1]], strokeColor=color,
              strokeWidth=w, strokeStyle="dashed" if dash else "solid",
              startArrowhead=start, endArrowhead=head, roundness={"type": 2})
    _elements.append(el)
    return el


def curved(x, y, pts, color=INK, w=2, dash=False, head="arrow", start=None):
    el = base("arrow", x, y, points=pts, strokeColor=color, strokeWidth=w,
              strokeStyle="dashed" if dash else "solid", startArrowhead=start,
              endArrowhead=head, roundness={"type": 2})
    _elements.append(el)
    return el


def line(x1, y1, x2, y2, color=INK, w=2, dash=False):
    el = base("line", x1, y1, points=[[0, 0], [x2 - x1, y2 - y1]], strokeColor=color,
              strokeWidth=w, strokeStyle="dashed" if dash else "solid")
    _elements.append(el)
    return el


def box(x, y, w, h, label, size=16, fill="transparent", stroke=INK, color=INK, rx=True):
    rect(x, y, w, h, fill=fill, stroke=stroke, rx=rx)
    text(label, x + w / 2, y + h / 2, size=size, align="center", anchor="cm", color=color)


def stick(cx, top, color=INK):
    ellipse(cx - 10, top, 20, 20, stroke=color)
    line(cx, top + 20, cx, top + 50, color=color)
    line(cx, top + 30, cx - 15, top + 45, color=color)
    line(cx, top + 30, cx + 15, top + 45, color=color)
    line(cx, top + 50, cx - 15, top + 70, color=color)
    line(cx, top + 50, cx + 15, top + 70, color=color)


def cylinder(x, y, w, h, label="Database", fill=GRAY_F, stroke=GRAY, size=16):
    e = 26
    ellipse(x, y, w, e, fill=fill, stroke=stroke)
    ellipse(x, y + h - e, w, e, fill=fill, stroke=stroke)
    rect(x, y + e / 2, w, h - e, fill=fill, stroke=stroke, rx=False)
    text(label, x + w / 2, y + h / 2 + 4, size=size, align="center", anchor="cm", color=SUBTLE)


def person(cx, top, color=INK):
    """Stick-figure user, matching excalidraw-example/excal.py."""
    stick(cx, top, color)


def monitor(x, y, w, h, label="", size=15, fill=BLUE_F, stroke=BLUE, color=SUBTLE):
    """A computer / client screen (screen + stand)."""
    rect(x, y, w, h, fill=fill, stroke=stroke, rx=True)
    line(x + w / 2, y + h, x + w / 2, y + h + 14, color=stroke)
    line(x + w * 0.30, y + h + 14, x + w * 0.70, y + h + 14, color=stroke, w=2)
    if label:
        text(label, x + w / 2, y + h / 2, size=size, align="center", anchor="cm", color=color)


def server(x, y, w, h, label="", size=15, fill=GREEN_F, stroke=GREEN, color=SUBTLE):
    """A server rack: stacked units with status dots."""
    rect(x, y, w, h, fill=fill, stroke=stroke, rx=True)
    n = 3
    for i in range(1, n):
        line(x + 8, y + h * i / n, x + w - 8, y + h * i / n, color=stroke, w=1)
    for i in range(n):
        ellipse(x + 12, y + h * (2 * i + 1) / (2 * n) - 3, 7, 7, fill=stroke, stroke=stroke)
    if label:
        text(label, x + w / 2 + 8, y + h / 2, size=size, align="center", anchor="cm", color=color)


def credit(s, x=1000, y=560):
    text(s, x, y, size=12, color=SEMANTIC["slate"], align="right", anchor="rb")


def badge(cx, cy, n, color=ORANGE, r=17):
    ellipse(cx - r, cy - r, r * 2, r * 2, fill=color, stroke=color)
    _elements[-1]["fillStyle"] = "solid"
    text(str(n), cx, cy, size=16, color=SEMANTIC["white"], align="center", anchor="cm")


def new():
    global _elements
    _elements = []


def _is_watermark(el):
    # Drop bare-domain credit text left by credit() (e.g. "scaleyourapp.com").
    if el.get("type") == "text" and re.fullmatch(r"[A-Za-z0-9.-]+\.[A-Za-z]{2,}", (el.get("text") or "").strip()):
        return True
    return False


def save(name):
    data = {"type": "excalidraw", "version": 2, "source": "https://excalidraw.com",
            "elements": [e for e in _elements if not _is_watermark(e)], "appState": {"gridSize": None, "viewBackgroundColor": SEMANTIC["white"]},
            "files": {}}
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, name + ".excalidraw"), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=1, ensure_ascii=False)
    print("wrote", name, "(%d elements)" % len(_elements))


# ---------------------------------------------------------------- diagrams
def d_ranks():
    new()
    box(50, 90, 410, 210, "", stroke=GRAY)
    box(560, 90, 440, 210, "", stroke=GRAY)
    text("At Point T In Time", 255, 115, 20, align="center", anchor="ct")
    text("At Point T+1 In Time", 780, 115, 20, align="center", anchor="ct")
    text("Scores:", 78, 175, 16, anchor="lm", color=SUBTLE)
    text("Scores:", 588, 175, 16, anchor="lm", color=SUBTLE)
    for i, s in enumerate(["3", "5", "2", "1", "...", "N"]):
        box(80 + i * 58, 205, 48, 48, s, size=18, fill=BLUE_F, stroke=BLUE)
    for i, s in enumerate(["3", "4", "6", "3", "2", "...", "N"]):
        box(588 + i * 51, 205, 44, 44, s, size=18, fill=GREEN_F, stroke=GREEN)
    text("players' scores change when they perform an\nactivity -> ranks are re-computed",
         505, 130, 14, align="center", anchor="ct", color=SUBTLE, width=180)
    arrow(470, 225, 552, 225)
    text("Updating Player Ranks", 505, 360, 26, align="center", anchor="ct")
    text("scaleyourapp.com", 40, 420, size=12, color=SEMANTIC["slate"], anchor="lt")
    save("Illustration 1.2")


def d_three_body(stars, planet, caption):
    new()
    cx, cy = 490, 320
    ellipse(cx - 300, cy - 160, 600, 320, stroke=SEMANTIC["borderLight"], dash=True)
    ellipse(cx - 250, cy - 205, 500, 410, stroke=SEMANTIC["borderLight"], dash=True)
    _elements[-1]["angle"] = 0.62
    ellipse(cx - 250, cy - 205, 500, 410, stroke=SEMANTIC["borderLight"], dash=True)
    _elements[-1]["angle"] = -0.62

    pos = [(215, 140), (835, 235), (395, 545)]
    cols = [(YELLOW, YELLOW_F), (ORANGE, ORANGE_F), (RED, RED_F)]
    for i, ((sx, sy), lab, (c, f)) in enumerate(zip(pos, stars, cols)):
        ellipse(sx - 36, sy - 36, 72, 72, fill=f, stroke=c)
        text(lab, sx, sy - 58, 20, align="center", anchor="ct", color=SUBTLE)
        curved(sx, sy, [[0, 0], [(cx - sx) * 0.5, (cy - sy) * 0.5 - 30], [cx - sx, cy - sy]],
               color=c, dash=True, head="triangle")

    if planet == "You":
        person(cx, cy - 36, color=BLUE)
        text("You", cx, cy + 66, 20, align="center", anchor="ct", color=BLUE)
    else:
        ellipse(cx - 26, cy - 26, 52, 52, fill=BLUE_F, stroke=BLUE)
        text(planet, cx, cy + 40, 20, align="center", anchor="ct", color=BLUE)
    text(caption, cx, 700, 15, align="center", anchor="ct", color=SUBTLE, width=820)
    text("the three-body problem", 490, 645, 26, align="center", anchor="ct")
    save("Illustration 1.5" if stars == ["Star A", "Star B", "Star C"] else "Illustration 1.6")


def d_roadmap():
    new()
    nodes = [(80, 80, "First Milestone\nLearn the domain fundamentals"),
             (520, 200, "Second Milestone\nMastering DSA and Problem Solving"),
             (80, 320, "Third Milestone\nDevelop Simple Practice Projects"),
             (520, 440, "Fourth step\nFinal Project"),
             (80, 560, "Fifth step\nMake the Switch")]
    w, h = 300, 96
    for i, (x, y, lab) in enumerate(nodes):
        first = lab.split("\n")[0]
        box(x, y, w, h, lab, size=15, fill=BLUE_F, stroke=BLUE)
        badge(x - 26 if x < 300 else x + w + 26, y + h / 2, i + 1)
    arrow(380, 128, 520, 245)
    arrow(670, 296, 380, 365)
    arrow(380, 368, 520, 485)
    arrow(670, 536, 380, 605)
    text("Developer Roadmap", 470, 700, 28, align="center", anchor="ct")
    save("Illustration 1.8")


def d_fullstack():
    new()
    UI = ["User Interface", "", "HTML", "CSS", "JavaScript", "React", "Angular", "Vue"]
    BE = ["Backend App Module", "", "Core Java", "Java EE", "Spring"]
    DB = ["Database", "", "Relational (SQL)", "NoSQL"]
    box(40, 120, 280, 250, "\n".join(UI), size=17, fill=BLUE_F, stroke=BLUE)
    box(360, 120, 260, 250, "\n".join(BE), size=17, fill=GREEN_F, stroke=GREEN)
    box(660, 120, 280, 250, "\n".join(DB), size=17, fill=ORANGE_F, stroke=ORANGE)
    monitor(150, 45, 80, 55)
    server(455, 45, 80, 58)
    cylinder(760, 42, 80, 66, "")
    arrow(322, 245, 356, 245, start="arrow")
    arrow(622, 245, 656, 245, start="arrow")
    text("Full Stack Developer", 490, 410, 26, align="center", anchor="ct")
    save("Illustration 1.9")


def d_iobound():
    new()
    monitor(70, 170, 230, 150, "Game Client", size=17)
    person(70, 360, color=BLUE)
    text("Player", 70, 445, 14, align="center", anchor="ct", color=SUBTLE)
    server(390, 170, 230, 150, "Backend Server")
    cylinder(760, 170, 180, 170, "Database")
    arrow(302, 225, 388, 225, head="arrow")
    arrow(388, 270, 302, 270, head="arrow")
    text("requests", 345, 195, 14, align="center", anchor="ct", color=SUBTLE)
    arrow(622, 225, 758, 225, head="arrow")
    arrow(758, 270, 622, 270, head="arrow")
    text("IO operations", 690, 195, 14, align="center", anchor="ct", color=SUBTLE)
    text("The server waits on IO (disk / network / DB) to respond.\nThe faster the IO, the faster the response.",
         520, 470, 16, align="center", anchor="ct", color=SUBTLE, width=760)
    text("IO-bound service", 520, 530, 24, align="center", anchor="ct")
    save("Illustration 1.10")


def d_memorybound():
    new()
    person(120, 30, color=BLUE)
    text("User", 120, 104, 18, align="center", anchor="ct", color=BLUE)
    text("Microservices leveraging in-memory databases along with the primary databases\nto cut down the response latency",
         600, 40, 16, align="center", anchor="ct", color=SUBTLE, width=720)
    svcs = [(60, "Product\nSearch"), (380, "User\nFeedback"), (700, "Order\nManagement")]
    for x, name in svcs:
        box(x, 200, 240, 90, name, size=17, fill=GREEN_F, stroke=GREEN)
        cylinder(x + 40, 330, 160, 120, "In-memory Database", fill=TEAL_F, stroke=TEAL, size=13)
        arrow(120, 118, x + 120, 198, head="arrow")
        arrow(x + 120, 292, x + 120, 328, start="arrow")
    for x, _ in svcs:
        cylinder(x + 40, 520, 160, 120, "Primary Database", size=13)
        arrow(x + 120, 452, x + 120, 518, start="arrow")
    text("Primary databases for respective microservices", 500, 670, 16,
         align="center", anchor="ct", color=SUBTLE)
    save("Illustration 1.11")


def d_sync():
    new()
    person(80, 205, color=BLUE)
    person(150, 235, color=BLUE)
    text("Clients", 115, 320, 18, align="center", anchor="ct", color=BLUE)
    reqs = ["R1", "R2", "...", "Rn"]
    for i, r in enumerate(reqs):
        text(r, 205, 215 + i * 45, 14, anchor="lm", color=SUBTLE)
    box(330, 110, 400, 360, "", stroke=GREEN)
    text("Application Server", 530, 135, 20, align="center", anchor="ct", color=GREEN)
    threads = ["Thread T1  -  handling R1  (blocked)", "Thread T2  -  handling R2  (blocked)",
               "Thread T3  -  handling R3  (blocked)", "...", "Thread Tn  -  handling Rn  (blocked)"]
    for i, t in enumerate(threads):
        text(t, 360, 195 + i * 55, 15, anchor="lm", color=SUBTLE)
    cylinder(800, 200, 170, 170, "Database")
    for i in range(4):
        y = 210 + i * 55
        arrow(205, y + 10, 328, y + 10, head="arrow", color=GRAY)
        arrow(732, y + 10, 798, y + 10, head="arrow", color=GRAY, dash=True)
    text("IO calls", 765, 175, 13, align="center", anchor="ct", color=SUBTLE)
    text("Each worker thread is blocked while it waits for the database.\nA blocked thread cannot serve other requests -> contention.",
         530, 500, 16, align="center", anchor="ct", color=SUBTLE, width=820)
    text("Synchronous thread-per-request model", 530, 560, 24, align="center", anchor="ct")
    save("Illustration 1.12")


def d_async():
    new()
    person(90, 215, color=BLUE)
    text("Clients\n(R1 ... Rn)", 90, 300, 15, align="center", anchor="ct", color=BLUE)
    box(260, 120, 430, 360, "", stroke=TEAL)
    text("Node.js Server", 475, 140, 20, align="center", anchor="ct", color=TEAL)
    box(300, 200, 130, 240, "Event\nQueue\n\nR1\nR2\n...\nRn", size=15, fill=TEAL_F, stroke=TEAL)
    ellipse(520, 275, 130, 130, fill=TEAL_F, stroke=TEAL)
    text("Event\nLoop", 585, 340, 17, align="center", anchor="cm", color=TEAL)
    box(730, 180, 230, 130, "Kernel Threads\n(OS thread pool)", size=15, fill=GRAY_F, stroke=GRAY)
    cylinder(770, 400, 180, 150, "Database")
    arrow(135, 300, 298, 300, head="arrow")
    arrow(432, 320, 518, 335, head="arrow")
    text("delegate IO\n(non-blocking)", 690, 150, 14, align="center", anchor="ct", color=SUBTLE)
    arrow(650, 320, 728, 245, head="arrow")
    arrow(845, 312, 860, 398, head="arrow")
    curved(860, 398, [[0, 0], [60, -150], [-160, -150]], color=SUBTLE, dash=True, head="arrow")
    text("callback", 700, 380, 13, color=SUBTLE)
    text("IO is delegated to the kernel; the single event loop never blocks.", 540, 510, 15,
         align="center", anchor="ct", color=SUBTLE, width=760)
    text("Asynchronous single-threaded event loop architecture", 540, 555, 22,
         align="center", anchor="ct")
    save("Illustration 1.13")


def d_actors():
    new()
    rect(60, 110, 860, 400, fill="transparent", stroke=GRAY, dash=True)
    text("Cluster", 82, 130, 18, anchor="lm", color=GRAY)
    nodes = {"Node A": (150, 190), "Node B": (560, 190), "Node C": (150, 370), "Node D": (560, 370)}
    centers = {}
    for name, (x, y) in nodes.items():
        box(x, y, 240, 140, "", stroke=PURPLE)
        text(name, x + 120, y + 22, 16, align="center", anchor="ct", color=PURPLE)
        for i in range(3):
            ax = x + 70 + i * 50
            ellipse(ax - 13, y + 80, 26, 26, fill=PURPLE_F, stroke=PURPLE)
        centers[name] = (x + 120, y + 70)
    pairs = [("Node A", "Node B"), ("Node A", "Node C"), ("Node B", "Node D"),
             ("Node C", "Node D"), ("Node A", "Node D"), ("Node B", "Node C")]
    for a, b in pairs:
        (x1, y1), (x2, y2) = centers[a], centers[b]
        curved((x1 + x2) / 2, (y1 + y2) / 2,
               [[-(x2 - x1) / 2, -(y2 - y1) / 2], [0, 0], [(x2 - x1) / 2, (y2 - y1) / 2]],
               color=ORANGE, start="arrow", head="arrow")
    text("Gossip protocol (peer-to-peer)", 490, 530, 15, align="center", anchor="ct", color=ORANGE)
    text("Actors communicating with each other in the cluster in a peer-to-peer\nfashion with the help of the Gossip protocol",
         490, 28, 16, align="center", anchor="ct", color=SUBTLE, width=820)
    save("Illustration 1.14")


def d_cache():
    new()
    box(40, 90, 420, 380, "", stroke=GRAY)
    box(560, 90, 420, 380, "", stroke=GRAY)
    text("Before", 250, 110, 22, align="center", anchor="ct")
    text("After", 770, 110, 22, align="center", anchor="ct")
    server(120, 160, 170, 90, "App Server", size=15)
    cylinder(140, 320, 170, 120, "Database")
    for dy in (-15, 0, 15):
        arrow(205, 252 + dy, 225, 318 + dy, head="arrow", color=GRAY)
        arrow(225, 318 + dy, 205, 252 + dy, head="arrow", color=GRAY)
    text("every read / write hits the database\n(expensive)", 250, 470, 14,
         align="center", anchor="ct", color=SUBTLE)
    server(620, 150, 160, 80, "App Server", size=13)
    box(800, 150, 150, 80, "Cache", size=16, fill=YELLOW_F, stroke=YELLOW)
    cylinder(800, 330, 150, 110, "Database", size=14)
    arrow(782, 175, 798, 175, head="arrow", color=GREEN, w=3)
    arrow(798, 210, 782, 210, head="arrow", color=GREEN, w=3)
    text("cheap\nread / writes", 770, 250, 13, align="center", anchor="ct", color=GREEN)
    curved(875, 232, [[0, 0], [30, 50], [0, 96]], color=ORANGE, dash=True, head="arrow")
    text("batch job updates periodically", 940, 300, 13, align="right", anchor="rm", color=ORANGE)
    text("A trade-off: keep hot data in a cache and sync the database in batches.\nFaster and cheaper, but a cache failure can lose in-flight state.",
         510, 500, 15, align="center", anchor="ct", color=SUBTLE, width=900)
    save("Illustration 1.15")


def d_timeline():
    new()
    ox, oy = 130, 470
    line(ox, oy, 880, oy, w=2)
    line(ox, oy, ox, 100, w=2)
    arrow(870, oy, 900, oy, head="arrow")
    arrow(ox, 110, ox, 90, head="arrow")
    text("Time", 905, oy, 18, anchor="lm")
    text("Features", ox - 10, 85, 18, align="right", anchor="rb")
    pts = [[0, 0], [140, -40], [250, -60], [360, -150], [500, -210], [620, -300], [730, -360]]
    curved(ox, oy, pts, color=GREEN, w=3, head="arrow")
    for gx in (ox, 300, 480, 660, 860):
        line(gx, oy, gx, oy + 6, w=1, color=GRAY)
    line(710, oy, 710, 120, dash=True, color=RED)
    text("Soft deadline", 710, 100, 15, align="center", anchor="cb", color=RED)
    arrow(ox, oy, ox, 440, head="arrow", color=BLUE)
    text("Project start day", ox, oy + 12, 15, align="center", anchor="ct", color=BLUE)
    text("Get the skeleton / MVP ready first,\nthen add features one by one.",
         250, 250, 15, align="left", anchor="lt", color=SUBTLE, width=260)
    text("Be brutal: cut the 'good to have' features,\nkeep the 'must have' ones.",
         560, 380, 15, align="left", anchor="lt", color=SUBTLE, width=300)
    text("Building a project from the bare bones", 490, 30, 24, align="center", anchor="ct")
    # supportive drawings: a little flag on the soft deadline + a person at the start
    line(710, 120, 710, 88, color=RED)
    curved(710, 88, [[0, 0], [24, 8], [0, 16]], color=RED, head=None)
    person(ox, 515, color=BLUE)
    text("Today", ox, 600, 14, align="center", anchor="ct", color=BLUE)
    save("Illustration 1.16")


def d_twitter():
    new()
    rect(40, 40, 820, 330, fill=SEMANTIC["white"], stroke=GRAY)
    ellipse(80, 80, 64, 64, fill=BLUE_F, stroke=BLUE)
    text("MH", 112, 112, 22, align="center", anchor="cm", color=BLUE)
    text("Max Howell", 165, 84, 20)
    text("@mxcl", 165, 114, 16, color=GRAY)
    text("\u201cGoogle: 90% of our engineers use the software you wrote (Homebrew),\n"
         "but you can\u2019t invert a binary tree on a whiteboard so f*** off.\u201d",
         80, 180, 19, width=740)
    text("10:37 PM \u00b7 Jun 10, 2015 \u00b7 Twitter Web Client", 80, 300, 15, color=GRAY)
    line(80, 328, 820, 328, w=1, color=SEMANTIC["surfaceMuted"])
    text("7,576 Retweets      518 Quote Tweets      14.8K Likes", 80, 345, 15, color=GRAY)
    save("Twitter")


def main():
    # Illustration 1.1 is the identical "Scalable Application" figure the user
    # already recreated by hand -> copy it verbatim.
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "library", "scalable_application.excalidraw")
    src = os.path.normpath(src)
    if os.path.exists(src):
        with open(src, encoding="utf-8") as f:
            data = json.load(f)
        data["elements"] = [e for e in data.get("elements", []) if not _is_watermark(e)]
        with open(os.path.join(OUT, "Illustration 1.1.excalidraw"), "w", encoding="utf-8") as f:
            json.dump(data, f, indent=1, ensure_ascii=False)
        print("wrote Illustration 1.1 (copied from scalable_application.excalidraw)")

    d_ranks()
    d_three_body(["Star A", "Star B", "Star C"], "Planet",
                 "The unpredictable pull of the stars keeps the planet's conditions chaotic.")
    d_three_body(["Web Dev", "ML", "DSA"], "You",
                 "Our careers are continually swayed by the other domains we could have chosen.")
    d_roadmap()
    d_fullstack()
    d_iobound()
    d_memorybound()
    d_sync()
    d_async()
    d_actors()
    d_cache()
    d_timeline()
    d_twitter()
    # 1.17 is the same 'Developer Roadmap' figure as 1.8
    with open(os.path.join(OUT, "Illustration 1.8.excalidraw"), encoding="utf-8") as f:
        rm = f.read()
    with open(os.path.join(OUT, "Illustration 1.17.excalidraw"), "w", encoding="utf-8") as f:
        f.write(rm)
    print("wrote Illustration 1.17 (same Developer Roadmap figure as 1.8)")


if __name__ == "__main__":
    main()
