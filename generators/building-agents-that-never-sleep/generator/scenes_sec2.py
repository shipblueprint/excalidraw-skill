#!/usr/bin/env python3
"""scenes_sec2.py — Section 2 "Setup" diagrams (lessons 006-011).

006-010 were rebuilt on the user's simplified library (scenes_lib) in the
scalable_application style; 006 uses the ekit timeline idiom. 011 is unchanged.
Run:  python3 scenes_sec2.py   (writes *.excalidraw next to this file)
"""
from ekit import *
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "builders"))
from scenes_lib import (place, metrics, REF_BG, hdr, cap, rref, eref, panel,
                        BLACK, MID, ACC, GRAY, GREEN, WHITE, file_name)


def _person(comp, x, y, label, scale=1.0):
    place(comp, x, y, scale=scale, retag={"User": label, "Node": ""})


def _device(x, y, label, scale=1.0):
    place("computer", x, y, scale=scale, retag={"Node": label})


def d_006():
    """The repo and branches — main + lesson-1..6."""
    new()
    hdr("The Repo and Branches", 60, 36)
    text("One repository, seven branches. Each lesson sits on its own branch.", 60, 76, size=15, color=MID, width=760)
    line(80, 320, 1380, 320, color=BLACK, w=3)
    text("main — the finished app", 80, 296, size=13, color=MID)
    badge(200, 320, 1, r=16, fill=ACC)
    for i, (bx, label, note) in enumerate([
        (380, "lesson-1", "goal + loop"),
        (560, "lesson-2", "durable steps"),
        (740, "lesson-3", "wait for input"),
        (920, "lesson-4", "approvals"),
        (1100, "lesson-5", "safe retries"),
        (1280, "lesson-6", "ask for help"),
    ]):
        top = i % 2 == 0
        line(bx, 320, bx, 210 if top else 430, color=MID, w=2)
        rref(bx - 70, 150 if top else 440, 140, 46)
        text(label, bx, 173 if top else 463, size=13, align="center", anchor="cm", color=BLACK)
        text(note, bx, 208 if top else 500, size=11, color=MID, align="center", anchor="ct", width=120)
    _device(1210, 255, "git clone …", scale=1.1)
    cap("one machine, many branches", 1262, 415, size=12)
    text("check out the branch of the lesson you're learning —\nthe code on main is the finished blueprint", 540, 585, size=12, color=MID, align="center", width=520)
    save(file_name(6)[:-5], bg=REF_BG)


def d_007():
    """Setting up your environment."""
    new()
    hdr("Setting Up Your Environment", 60, 36)
    text("Five minutes: a database, a key, and a schema.", 60, 76, size=15, color=MID, width=680)

    panel(60, 150, 660, 470, "Step 1 — the database (Neon)")
    place("cloud", 110, 200, scale=1.1, retag={"cloud": "Neon Postgres"})
    cap("the Postgres you get\nin 60 seconds", 260, 330, size=13, width=220)
    database(400, 205, 130, 110, "", fill="transparent", stroke=BLACK, color=BLACK)
    text("connection string → .env", 465, 340, size=13, align="center", anchor="ct", color=BLACK)
    cap("free tier · created in a minute\npaste DATABASE_URL into .env", 380, 470, size=13, width=280)

    panel(780, 150, 600, 470, "Step 2 — the key")
    text("OpenAI API key", 1080, 200, size=15, align="center", anchor="ct", color=BLACK)
    rref(880, 240, 400, 70, fill=WHITE)
    text("sk-…", 1080, 275, size=16, align="center", anchor="cm", color=ACC)
    _device(900, 350, "terminal", scale=1.0)
    cap("export OPENAI_API_KEY=sk-…", 1120, 400, size=13, width=260)
    cap("any model works — the harness calls it\nonce per decision; a couple of dollars\nlasts forever", 1080, 505, size=13, width=340)

    text(".env → DATABASE_URL, OPENAI_API_KEY", 60, 660, size=14, color=BLACK)
    text("npm run db:push · npm run pre-flight · npm run db:seed", 60, 700, size=14, color=BLACK)
    save(file_name(7)[:-5], bg=REF_BG)


def d_008():
    """Running the app — three dev servers, event pipeline through a queue."""
    new()
    hdr("Running the App", 60, 36)
    text("Three terminals, three servers, one event pipeline.", 60, 76, size=15, color=MID, width=680)

    place("app_server", 90, 190, retag={"Application\nserver": "npm run\ndev:checkout"})
    cap("the fake service that breaks", 138, 296, size=13)
    place("msgq", 310, 165, scale=0.85)
    cap("events", 358, 296, size=12)
    place("app_server", 570, 190, retag={"Application\nserver": "npm run\ndev:agent"})
    cap("the API + Ingest\nworkflow executor", 618, 296, size=13)
    _device(1080, 190, "npm run\ndev", scale=1.2)
    cap("the incident\ndashboards (UI)", 1125, 352, size=13)

    arrow(186, 237, 310, 237, color=BLACK, w=2)
    arrow(404, 237, 570, 237, color=BLACK, w=2)
    cap("incident events", 490, 222, size=12)
    arrow(666, 237, 1080, 237, color=ACC, w=3)
    cap("decisions + reports", 873, 222, size=12)

    _person("user", 130, 480, "Customer")
    cap("a checkout happens…", 180, 720, size=13)
    _person("you", 1180, 480, "You")
    cap("…and you're asleep", 1230, 720, size=13)
    text("Ingest dev dashboard: 127.0.0.1:8288/runs — watch runs, replay steps, fire test events", 700, 640, size=13, color=MID, width=620)
    save(file_name(8)[:-5], bg=REF_BG)


def d_009():
    """Simulating faults."""
    new()
    hdr("Simulating Faults", 60, 36)
    text("Break the service on purpose, and make it recover on its own.", 60, 76, size=15, color=MID, width=740)

    place("app_server", 120, 200, retag={"Application\nserver": "Checkout\nService"})
    cap("either healthy… or not", 168, 306, size=13)
    rref(560, 190, 300, 130, fill=WHITE, stroke=ACC)
    text("npm run checkout\n--fault feature", 710, 240, size=14, align="center", anchor="ct", color=BLACK)
    arrow(216, 247, 560, 247, color=ACC, w=3)
    cap("degraded! error rate spikes", 388, 232, size=12, width=150)

    panel(960, 150, 460, 480, "Fault flags")
    for i, (flag, what) in enumerate([
        ("--fault feature", "a feature breaks"),
        ("--fault dependency", "upstream service down"),
        ("--alerts N", "how many alerts to fire"),
        ("--interval S", "seconds between alerts"),
        ("--self-recover", "heals after a while"),
    ]):
        text(flag, 980, 210 + i * 62, size=13, color=BLACK)
        text("→ " + what, 1240, 210 + i * 62, size=12, color=MID, width=200)
    cap("every fault is an honest incident:\nan event shows up in the Events tab", 260, 520, size=13, width=520)
    save(file_name(9)[:-5], bg=REF_BG)


def d_010():
    """The incident dashboard — Inbox / Activities / Events."""
    new()
    hdr("The Incident Dashboard", 60, 36)
    text("Three tabs, one story: events in, agent work in the middle, humans on the right.", 60, 76, size=15, color=MID, width=820)

    _device(90, 170, "dashboard", scale=1.5)
    cap("live when you are", 150, 372, size=13)
    _person("user", 90, 440, "you", scale=0.9)
    cap("the human,\nin control", 135, 662, size=13)

    place("dash2", 560, 180, scale=1.3)
    place("dash1", 750, 180, scale=1.3)
    place("dash4", 940, 180, scale=1.3)
    text("Inbox", 631, 374, size=14, align="center", anchor="ct", color=BLACK)
    text("Activities", 821, 374, size=14, align="center", anchor="ct", color=BLACK)
    text("Events", 1011, 374, size=14, align="center", anchor="ct", color=BLACK)
    rref(560, 420, 110, 42, fill=GREEN, stroke=GREEN)
    text("Approve", 615, 441, size=13, align="center", anchor="cm", color=WHITE)
    rref(690, 420, 110, 42, fill=WHITE, stroke=BLACK)
    text("Reject", 745, 441, size=13, align="center", anchor="cm", color=BLACK)
    cap("every decision recorded,\nevery step replayable", 820, 440, size=12, width=180)
    cap("events arrive by webhook —\nincident/opened and friends", 1010, 440, size=12, width=180)

    rref(1140, 170, 250, 420)
    text("the story", 1265, 190, size=15, align="center", anchor="ct", color=BLACK)
    for i, s in enumerate([
        "1. event fires (webhook)",
        "2. agent wakes & works",
        "3. needs input → inbox",
        "4. you approve / reject",
        "5. run ends, report written",
    ]):
        text(s, 1160, 235 + i * 44, size=13, color=BLACK, width=220)
    cap("events in, work in the\nmiddle, humans on the right", 1265, 560, size=12, width=230)
    save(file_name(10)[:-5], bg=REF_BG)


def d_011():
    """Tour of the finished app — the full incident story."""
    new()
    hdr("Tour of the Finished App", 60, 36)
    text("One incident, from alert to recovery — the story every later lesson builds toward.", 60, 76, size=15, color=MID, width=820)
    steps = [
        ("incident\nopened", CON, BDR),
        ("observe\nstate", CON, BDR),
        ("decide\ninspect logs", CON, BDR),
        ("propose\nrollback", ACC, ACC),
        ("human\napproves", ACC, ACC),
        ("execute\nrollback", CON, BDR),
        ("verify\nhealthy", CON, BDR),
    ]
    x = 60
    for i, (label, fill, stroke) in enumerate(steps):
        box(x, 190, 150, 110, label, size=13, fill=fill, stroke=stroke)
        if i < len(steps) - 1:
            arrow(x + 150, 245, x + 190, 245, color=BLACK, w=2)
        x += 190
    badge(135, 172, 1, r=16, fill=ACC)
    text("blocked — waiting on a human", 705, 330, size=12, color=ACC, align="center", anchor="ct", width=170)
    text("every step is a checkpointed step of a durable run", 60, 430, size=12, color=MID, width=520)
    text("the run ends with a written report, not a wall of chat text", 60, 465, size=12, color=MID, width=520)
    arrow(875, 300, 1210, 540, color=ACC, dash=True, w=2)
    _person("you", 1160, 560, "you", scale=0.8)
    cap("you — the human —\nat your own pace", 1215, 762, size=13)
    save(file_name(11)[:-5], bg=REF_BG)


if __name__ == "__main__":
    for fn in (d_006, d_007, d_008, d_009, d_010, d_011):
        fn()
        print("wrote", fn.__name__)