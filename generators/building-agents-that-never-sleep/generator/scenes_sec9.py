#!/usr/bin/env python3
"""
scenes_sec9.py — Section 9 "Wrap-up" diagrams (lessons 049-052).

Rebuilt on the user's simplified library (scenes_lib) in the
scalable_application style: black sw2 strokes, white canvas, fontFamily 1,
16-24px text; orange only for badges/incidents.
Run:  python3 scenes_sec9.py   (writes *.excalidraw next to this file)
"""
from ekit import *
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "builders"))
from scenes_lib import (place, metrics, REF_BG, hdr, cap, rref, eref, panel,
                        BLACK, MID, ACC, GRAY, GREEN, WHITE, file_name)
from common.tokens import SEMANTIC

BLUE = SEMANTIC["blue"]


def d_049():
    """The complete architecture."""
    new()
    hdr("The Complete Architecture", 60, 36)
    text("One stack, from doorbell to dashboard — and the runtime that holds it together.", 60, 76, size=15, color=MID, width=880)
    layers = [
        ("events — doorbells (incident/opened · updated · recovered)", CON, BDR),
        ("workflow = a React component that re-renders on every wake", WHITE, BLACK),
        ("steps — useMemo · one async thing each · cached by name+cycle", WHITE, BLACK),
        ("the harness — observe / decide / act, authority policies, version checks", ACC, ACC),
        ("guardrails — bounded loop · goal check · run guard · terminal statuses", WHITE, BLACK),
    ]
    for i, (lab, fill, stroke) in enumerate(layers):
        box(90, 150 + i * 100, 840, 80, lab, size=14, fill=fill, stroke=stroke)
    box(90, 660, 840, 80, "Ingest — durable execution (suspend · resume · memoize · retry)", size=14, fill=BLUE, stroke=BLUE, color=WHITE)
    dashed_group(1000, 150, 420, 250, "", size=12)
    browser(1020, 170, 380, 200, "", size=12)
    text("dashboard + inbox", 1100, 195, size=13, color=BLACK, width=200)
    text("runs · steps · cycles", 1040, 240, size=11, color=MID, width=200)
    text("approvals · help", 1040, 300, size=11, color=MID, width=200)
    text("events → re-run → resume\n→ complete. All recorded.", 1100, 470, size=12, color=MID, align="center", width=300)
    text("the durable runtime is the soul of the agent —\nthe LLM is the least important part", 420, 780, size=13, color=BLACK, align="center", width=800)
    save(file_name(49)[:-5], bg=REF_BG)


def d_050():
    """Capstone ideas."""
    new()
    hdr("Capstone Ideas", 60, 36)
    text("Three directions the workshop points at — each reuses the harness you have now.", 60, 76, size=15, color=MID, width=900)
    # email watcher
    acc_box(60, 160, 620, 180, "a personal email watcher", size=15)
    text("the agent fits an inbox: forward mail to the AI's own\naddress (agent-mail pattern) → events wake a run that\ntriages and drafts replies. ~70% = the harness you built.", 160, 250, size=12, color=BLACK, align="center", width=420)
    # browser agent
    acc_box(700, 160, 620, 180, "a browser agent", size=15)
    text("Browserbase · browser-use · Argos (~$25/mo): the agent\ngets an actual computer — install Codex, stream the\nscreen, browse like a person. Observation + actions.", 810, 250, size=12, color=BLACK, align="center", width=420)
    # employee harness
    acc_box(60, 380, 620, 180, "an employee harness for software dev", size=15)
    text("tools in the harness talk to hosted coding agents; the\nharness writes no code. Events from GitHub · Linear ·\nJira · Slack drive it — issues become runs.", 160, 470, size=12, color=BLACK, align="center", width=420)
    # homework
    box(700, 380, 620, 180, "homework", size=15, fill=WHITE, stroke=BLACK)
    text("build one. Feed it these notes. Then try to break it —\nduplicate events, stale state, refused help, an agent\nthat wants to loop forever. That is the final exam.", 810, 470, size=12, color=BLACK, align="center", width=420)
    save(file_name(50)[:-5], bg=REF_BG)


def d_051():
    """Alternative runtimes."""
    new()
    hdr("Alternative Runtimes", 60, 36)
    text("The durable-execution idea, served five ways — pick by where your compute lives.", 60, 76, size=15, color=MID, width=920)
    rows = [
        ("Ingest", "this course · event-driven · memoized steps · serverless", "select *", "doorbells + useMemo"),
        ("Temporal", "activities + workers · durable against time itself", "self-host / cloud", "perpetual workflows"),
        ("Vercel Workflows", "useWorkflow() — everything auto-converts to steps", "serverless", "zero new infra"),
        ("Upstash", "HTTP-based steps — a workflow is a chain of requests", "serverless / edge", "tiny steps"),
        ("DBOS", "durable execution inside Postgres transactions", "any postgres", "the DB is the runtime"),
    ]
    box(60, 150, 200, 44, "runtime", size=13, fill=CON, stroke=BDR)
    box(260, 150, 620, 44, "shape", size=13, fill=CON, stroke=BDR)
    box(880, 150, 440, 44, "where it runs", size=13, fill=CON, stroke=BDR)
    for i, (r, shape, where, note) in enumerate(rows):
        box(60, 200 + i * 76, 200, 66, r, size=13, fill=ACC if i == 0 else WHITE, stroke=BLACK if i == 0 else BDR)
        box(260, 200 + i * 76, 620, 66, shape, size=12, fill=WHITE, stroke=BDR)
        box(880, 200 + i * 76, 440, 66, where, size=12, fill=CON, stroke=BDR)
        text(note, 60, 240 + i * 76, size=10, color=MID, width=180)
    text("serverless freezes compute at a wait (cost: zero); Temporal pays workers to\nstay warm; locally we simulate freezes with while-loops. Same design, same soul.", 420, 610, size=12, color=MID, align="center", width=880)
    save(file_name(51)[:-5], bg=REF_BG)


def d_052():
    """Where background agents go next."""
    new()
    hdr("Where Background Agents Go Next", 60, 36)
    text("The reframe: a durable runtime turns a prompt loop into a live agent that runs forever.", 60, 76, size=15, color=MID, width=920)
    box(70, 220, 340, 120, "stateless prompt loop\n(ask · answer · forget)", size=13, fill=CON, stroke=BDR)
    arrow(410, 280, 520, 280, color=BLACK, w=3)
    acc_box(520, 200, 380, 160, "+ the durable runtime\n(events · steps · harness\n· guardrails)", size=16)
    arrow(900, 280, 1010, 280, color=BLACK, w=3)
    box(1010, 220, 360, 120, "a live agent\nthat never sleeps", size=14, fill=GREEN, stroke=GREEN, color=WHITE)
    for i, lab in enumerate(["multi-agent: a triage LLM decides\nwhich event feeds which run", "tool use: hosted coding agents,\nCodex + Claude tools as steps", "computer use: the agent owns a\nbrowser, a shell, a screen"]):
        box(120 + i * 380, 430, 340, 120, lab, size=12, fill=WHITE, stroke=BDR)
    text("build one — feed it these notes — and try to break it.\nThat is both the homework and the future: agents that run forever,\nand the runtime that keeps them honest.", 370, 640, size=13, color=BLACK, align="center", width=900)
    save(file_name(52)[:-5], bg=REF_BG)


if __name__ == "__main__":
    fns = [d_049, d_050, d_051, d_052]
    for fn in fns:
        fn()
        print("wrote", fn.__name__)