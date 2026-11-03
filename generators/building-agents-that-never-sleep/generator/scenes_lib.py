#!/usr/bin/env python3
"""
scenes_lib — compose scenes 001-010 from the user's simplified Excalidraw
library bundled in ./library (override with EXCALIDRAW_LIB_DIR):

    user.excalidraw              labeled person icon (head + terminal)
    you.excalidraw               same person icon + 4 dashboard-card widgets
    computer.excalidraw          terminal / device icon
    system-design.excalidraw     app-server cards, storage, message Q, cloud,
                                 load balancer, cache, DNS (sliced per label)
    scalable_application.excalidraw  style reference: black sw2 strokes,
                                 hachure fills, white canvas, fontFamily 1,
                                 body text 16-24.

Components are stored at absolute canvas offsets in their files, so `place()`
anchors each component's *visual* top-left corner at (x, y); line/arrow
elements extend by their points only (their width/height can be misleading).
The old excalidraw/libs/*.excalidrawlib copies are obsolete and unused.

Typical use (inside a scene generator):

    from scenes_lib import place, metrics, REF_BG, hdr, cap, panel, rref

    new()
    hdr("Welcome to the Course", 60, 36)
    place("app_server", 90, 170, retag={"Application\nserver": "Checkout\nService"})
    cap("the fake service that keeps breaking", 138, 280)
    save(file_name(1)[:-5], bg=REF_BG)
"""
import json
import os
import time
from ekit import _elements, _id, _nonce, rect, ellipse, text

LIB = os.environ.get("EXCALIDRAW_LIB_DIR") or os.path.join(os.path.dirname(os.path.abspath(__file__)), "library")
from ekit import BG, INK, ACC, MID, CON, BDR, WHITE
from common.tokens import SEMANTIC, FONT_UI
BLACK = SEMANTIC["black"]
GRAY = SEMANTIC["gray"]
GREEN = SEMANTIC["green"]
REF_BG = WHITE.lower()

_cache = {}
_sys_cache = {}


def _keep(e):
    """Drop giant canvas frames (the library files wrap every icon in a
    966x552 placeholder rectangle) and stray oversized shapes."""
    w, h = e.get("width", 0), e.get("height", 0)
    return w <= 240 and h <= 240


def _load(path):
    if path not in _cache:
        d = json.load(open(path, encoding="utf-8"))
        # NOTE: keep DELETED elements too — the simplified library marks most of
        # each icon's parts (terminal, widgets) as isDeleted, but they carry the
        # geometry we need. `place()` clears isDeleted so they render.
        _cache[path] = [e for e in d["elements"] if _keep(e)]
    return _cache[path]


# person/terminal icons: (x1, x2, y1, y2) region of the library file that holds
# the icon. user and you are the SAME person icon (head, neck, terminal box,
# cable, 'User'/'Node' labels) — its cluster in user.excalidraw has no stick
# figures, so both name it from that file.
_ICON_WINDOW = {
    "user":     (1988, 2120, 290, 560),   # person + terminal + labels
    "you":      (1988, 2120, 290, 560),
    "computer": (2000, 2140, 390, 530),   # terminal box + 'Node' label
}


# system-design slices: (center x, center y, radius, exact label text)
# The slice keeps the label text element plus any non-text shape whose bbox
# center falls inside the radius; arrows and stray texts are dropped.
_SPEC = {
    "app_server":   ((632, -117), 80,  "Application\nserver"),
    "multi_server": ((756, -135), 80,  "Multi\nInstance\nserver"),
    "server_bar":   ((430, 14),   80,  "server"),
    "multi_bar":    ((581, 17),   85,  "Multi Instance"),
    "cache":        ((467, 470),  92,  "Cache"),
    "dns":          ((789, 468),  92,  "DNS"),
    "msgq":         ((637, 622),  80,  "Message Q"),
    "loadbal":      ((455, 640), 100,  "Load\nBalancer"),
    "cloud":        ((440, 860),  92,  "cloud"),
}

# dashboard-card widgets inside you.excalidraw: (x1, x2, y1, y2) windows.
_DASH = {
    "dash1": (2025, 2138, 106, 250),
    "dash2": (2139, 2252, 105, 250),
    "dash3": (2025, 2138, 250, 396),
    "dash4": (2139, 2252, 251, 396),
}


def components(name):
    """Named component -> list of element dicts (cached).

    user / you : the library person icon (head + terminal + labels) — `you` is
    the same cluster, re-labelable via retag; computer : the terminal device
    icon; dash1..dash4 : the dashboard-card widgets inside you.excalidraw;
    everything else : a system-design slice.
    """
    if name in ("user", "you", "computer"):
        x1, x2, y1, y2 = _ICON_WINDOW[name]
        if name == "you":
            x1, x2, y1, y2 = _ICON_WINDOW["user"]
        return [e for e in _load(f"{LIB}/user.excalidraw"
                                 if name in ("user", "you") else
                                 f"{LIB}/computer.excalidraw")
                if x1 < e["x"] + e.get("width", 0) / 2 < x2
                and y1 < e["y"] + e.get("height", 0) / 2 < y2]
    if name in _DASH:
        x1, x2, y1, y2 = _DASH[name]
        return [e for e in _load(f"{LIB}/you.excalidraw")
                if e.get("type") != "text"
                and x1 < e["x"] + e.get("width", 0) / 2 < x2
                and y1 < e["y"] + e.get("height", 0) / 2 < y2]
    return _slice_sys(name)


def _slice_sys(name):
    if name in _sys_cache:
        return _sys_cache[name]
    (cx, cy), r, label = _SPEC[name]
    out = []
    for e in _load(f"{LIB}/system-design.excalidraw"):
        if e.get("type") == "arrow":
            continue
        if e.get("type") == "text":
            if e.get("text") == label:      # the component's own label only
                out.append(e)
            continue
        bx = e["x"] + e.get("width", 0) / 2
        by = e["y"] + e.get("height", 0) / 2
        if (bx - cx) ** 2 + (by - cy) ** 2 <= r * r:
            out.append(e)
    _sys_cache[name] = out
    return out


def _bbox(src):
    """Visual bounding box (x, y, w, h) in component coordinates. Lines and
    arrows extend by their points only; other elements by width/height."""
    x1 = y1 = float("inf")
    x2 = y2 = float("-inf")

    def add(cx, cy):
        nonlocal x1, y1, x2, y2
        x1 = min(x1, cx)
        y1 = min(y1, cy)
        x2 = max(x2, cx)
        y2 = max(y2, cy)

    for e in src:
        ex, ey = e["x"], e["y"]
        if e.get("type") in ("line", "arrow", "draw", "freedraw"):
            for p in e.get("points") or []:
                if isinstance(p, (list, tuple)) and len(p) >= 2:
                    add(ex + p[0], ey + p[1])
        else:
            add(ex, ey)
            add(ex + e.get("width", 0), ey)
            add(ex, ey + e.get("height", 0))
            add(ex + e.get("width", 0), ey + e.get("height", 0))
    return x1, y1, x2 - x1, y2 - y1


def metrics(name):
    """(x, y, w, h) of a component in its own coordinates (visual bbox)."""
    return _bbox(components(name))


def place(name, x, y, scale=1.0, retag=None, overrides=None):
    """Copy component `name` into the current scene with its visual top-left
    corner at (x, y).

    scale: uniform factor (geometry, points, fonts).
    retag: dict old-text -> new-text on text elements (use REAL newlines).
    overrides: optional {strokeColor/backgroundColor/strokeWidth} for all
           elements (re-tinting).
    Returns the placed elements (already appended to the scene).
    """
    src = components(name)
    x0, y0 = _bbox(src)[:2]
    idmap = {}
    out = []
    for e in src:
        n = dict(e)
        nid = _id()
        idmap[e["id"]] = nid
        n.update({
            "id": nid, "seed": _nonce(), "versionNonce": _nonce(),
            "updated": int(time.time() * 1000),
            "x": x + (e["x"] - x0) * scale,
            "y": y + (e["y"] - y0) * scale,
            "isDeleted": False,          # library marks icon parts deleted; revive
        })
        if scale != 1.0:
            n["width"] = e.get("width", 0) * scale
            n["height"] = e.get("height", 0) * scale
            if e.get("type") == "text":
                n["fontSize"] = e["fontSize"] * scale
                n["baseline"] = e.get("baseline", e["fontSize"]) * scale
            if isinstance(e.get("points"), list):
                n["points"] = [[p[0] * scale, p[1] * scale] for p in e["points"]]
        if e.get("type") == "text" and retag and e.get("text") in retag:
            n["text"] = retag[e["text"]]
            n["originalText"] = n["text"]
        if n.get("text") == "":          # retagged-to-empty labels: drop
            continue
        if n.get("type") == "text":
            # unify on the reference (scalable_application) text style:
            n.update({"fontFamily": FONT_UI, "lineHeight": 1.25, "strokeWidth": 2,
                      "strokeStyle": "solid", "verticalAlign": "top",
                      "backgroundColor": "transparent"})
        if overrides:
            n.update({k: v for k, v in overrides.items()
                      if k in ("strokeColor", "backgroundColor", "strokeWidth")})
        out.append(n)
    for n in out:
        cid = n.get("containerId")
        if cid in idmap:
            n["containerId"] = idmap[cid]
        elif cid:
            n["containerId"] = None      # bound to a dropped element: detach
        if n.get("frameId") in idmap:
            n["frameId"] = idmap[n["frameId"]]
        elif n.get("frameId"):
            n["frameId"] = None
        kept = []
        for b in n.get("boundElements") or []:
            if isinstance(b, dict) and b.get("id") in idmap:
                kept.append({**b, "id": idmap[b["id"]]})
        if kept:
            n["boundElements"] = kept
        elif "boundElements" in n:
            del n["boundElements"]
        n["groupIds"] = []
    _elements.extend(out)
    return out


# ---------------------------------------------------------------- scene pieces
def hdr(s, x, y, size=24, width=None):
    """Reference-style header: plain black text, no underline."""
    return text(s, x, y, size=size, color=BLACK, width=width)


def cap(s, x, y, size=13, width=None, color=MID, align="center", anchor="ct"):
    return text(s, x, y, size=size, width=width, color=color, align=align, anchor=anchor)


def rref(x, y, w, h, fill="transparent", stroke=BLACK, sw=2, dash=False, hch=False):
    """Reference-style rectangle (black sw2, optional hachure fill)."""
    el = rect(x, y, w, h, fill=fill, stroke=stroke, sw=sw, dash=dash)
    if hch or fill not in ("transparent", "none"):
        el["fillStyle"] = "hachure"
    return el


def eref(x, y, w, h, fill="transparent", stroke=BLACK, sw=2, dash=False, hch=False):
    """Reference-style ellipse."""
    el = ellipse(x, y, w, h, fill=fill, stroke=stroke, sw=sw, dash=dash)
    if hch or fill not in ("transparent", "none"):
        el["fillStyle"] = "hachure"
    return el


def panel(x, y, w, h, label=None, size=16, gap=12):
    """Reference-style outlined panel with an optional label above-left."""
    rref(x, y, w, h)
    if label:
        text(label, x + gap, y - gap - 6, size=size, color=BLACK)
    return None

_names = [
"001 Welcome and What You'll Build",
"002 What Is a Background Agent",
"003 Goals, Not Prompts",
"004 The Authority Problem",
"005 Anatomy of a Background Agent",
"006 The Repo and Branches",
"007 Setting Up Your Environment",
"008 Running the App",
"009 Simulating Faults",
"010 The Incident Dashboard",
"011 Tour of the Finished App",
"012 The Agent's World",
"013 The Action Set",
"014 The Workflow Function",
"015 Observing the World",
"016 Deciding with the LLM",
"017 Acting on the World",
"018 The Loop and Its Guardrails",
"019 Deterministic Goal Checks",
"020 Keeping an Audit Trail",
"021 Workshop Q&A_ Goals and the Loop",
"022 The One-Step Problem",
"023 Steps Are Checkpoints",
"024 Determinism and Idempotency",
"025 Business State vs Workflow State",
"026 Refactoring the Loop",
"027 A Step Is a useMemo",
"028 Action Policies",
"029 Demo_ The Agent Fixes an Outage",
"030 Choosing to Wait",
"031 Suspending a Run",
"032 step.waitForEvent",
"033 The Wait Loop",
"034 Wait or Ask for Help",
"035 One Harness, Many Runs",
"036 Why an Inbox, Not a Chat",
"037 Which Actions Need Approval",
"038 Proposing an Action",
"039 Waiting and Reconciling",
"040 Stale Proposals and Rejections",
"041 Demo_ Approving a Rollback",
"042 Idempotency Keys for Tool Calls",
"043 One Run per Incident",
"044 Step Retry Semantics",
"045 Guardrails and Budgets",
"046 The Ask-for-Help Action",
"047 Forcing a Re-Think",
"048 Demo_ The Agent Asks for Help",
"049 The Complete Architecture",
"050 Capstone Ideas",
"051 Alternative Runtimes",
"052 Where Background Agents Go Next",
]


def file_name(n):
    if 1 <= n <= len(_names):
        return _names[n - 1] + ".json"
    return f"{n:03d} Scene {n}.json"
