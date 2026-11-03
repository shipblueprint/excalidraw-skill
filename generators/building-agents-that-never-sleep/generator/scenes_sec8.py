#!/usr/bin/env python3
"""
scenes_sec8.py — Section 8 "Ask for Help" diagrams (lessons 046-048).

Rebuilt on the user's simplified library (scenes_lib) in the
scalable_application style: black sw2 strokes, white canvas, fontFamily 1,
16-24px text; orange only for badges/incidents.
Run:  python3 scenes_sec8.py   (writes *.excalidraw next to this file)
"""
from ekit import *
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "..", "common"))
# common on path above? ensure generators/common importable
from scenes_lib import (place, metrics, REF_BG, hdr, cap, rref, eref, panel,
                        BLACK, MID, ACC, GRAY, GREEN, WHITE, file_name)


def d_046():
    """The ask-for-help action."""
    new()
    hdr("The Ask-for-Help Action", 60, 36)
    text("Waiting and asking for help are non-destructive — so the model may decide them freely.", 60, 76, size=15, color=MID, width=900)
    box(80, 200, 300, 120, "decision:\n\"request help\"", size=13, fill=WHITE, stroke=BLACK)
    arrow(380, 260, 480, 260, color=ACC, w=3)
    box(480, 190, 360, 140, "policy: help\ninput = decision.detail\n(the question)", size=13, fill=CON, stroke=BDR)
    arrow(840, 260, 930, 260, color=BLACK, w=2)
    box(930, 190, 350, 140, "defer-help step +\nactivity: phase \"human\",\n\"help is not ready yet\"", size=12, fill=WHITE, stroke=BLACK)
    text("the help request goes to Slack or any interface\nyou watch — the reply is an event that wakes the run", 1140, 420, size=12, color=MID, align="center", width=420)
    arrow(930, 330, 720, 470, color=BLACK, w=2)
    acc_box(600, 470, 660, 110, "resume event: agent/approval.decided\n(one wake path for approvals and help)", size=13)
    text("approval decisions belong to the harness — help does not.\nThat asymmetry is the whole permission model.", 330, 660, size=12, color=ACC, align="center", width=780)
    save(file_name(46)[:-5], bg=REF_BG)


def d_047():
    """Forcing a re-think."""
    new()
    hdr("Forcing a Re-Think", 60, 36)
    text("The answer is not a directive to execute — it is new world state. Re-render, don't branch.", 60, 76, size=15, color=MID, width=920)
    box(80, 220, 300, 120, "human answers +\nhelp.decided event", size=12, fill=WHITE, stroke=BLACK)
    arrow(380, 280, 470, 280, color=ACC, w=3)
    acc_box(470, 210, 340, 140, "resume → policy: help\n→ if (policy === \"help\") continue", size=13)
    arrow(810, 280, 900, 280, color=BLACK, w=2)
    box(900, 210, 380, 140, "top of the loop:\nobserve — state now includes\nthe stored answer", size=12, fill=WHITE, stroke=BLACK)
    arrow(1090, 350, 1090, 440, color=BLACK, w=2)
    box(900, 440, 380, 120, "decide → act\n(connect the dots)", size=13, fill=GREEN, stroke=GREEN, color=WHITE)
    text("any relevant event re-renders the run against fresh state:\nthe answer is just the newest fact it observes", 300, 640, size=12, color=MID, align="center", width=800)
    save(file_name(47)[:-5], bg=REF_BG)


def d_048():
    """Demo: the agent asks for help."""
    new()
    hdr("Demo: The Agent Asks for Help", 60, 36)
    text("Dependency fault, no local fix — the agent asks, the world answers (one way or the other).", 60, 76, size=15, color=MID, width=920)
    steps = [
        ("dependency\nfault", CON, BDR),
        ("observe\n42 errors ·\nupstream down", WHITE, BLACK),
        ("decide:\nrequest help", ACC, ACC),
        ("paused:\n\"help is not\nready yet\"", WHITE, BDR),
        ("wake on\nhealth.recovered\nor human reply", WHITE, BDR),
        ("re-observe\nhealthy", GREEN, GREEN),
        ("completed", GREEN, GREEN),
    ]
    x = 40
    for i, (label, fill, stroke) in enumerate(steps):
        box(x, 200, 155, 130, label, size=11, fill=fill, stroke=stroke)
        if i < len(steps) - 1:
            arrow(x + 155, 265, x + 195, 265, color=BLACK, w=2)
        x += 195
    box(60, 430, 260, 90, "question payload\n\"can you restore the payment\ngateway, then notify us…\"", size=11, fill=CON, stroke=BDR)
    box(350, 430, 300, 90, "unexpected path:\nthe gateway recovers on its own —\nno human needed", size=11, fill=WHITE, stroke=BDR)
    box(690, 430, 300, 90, "expected path:\na human answers → same event\nwakes the run", size=11, fill=WHITE, stroke=BDR)
    box(1030, 430, 260, 90, "either way: re-observe →\nconnect the dots → complete\n(no LLM code changed)", size=11, fill=ACC, stroke=ACC, color=WHITE)
    text("it ended exactly where we wanted — the path was just unexpected. The harness made that safe.", 370, 620, size=13, color=BLACK, align="center", width=880)
    save(file_name(48)[:-5], bg=REF_BG)


if __name__ == "__main__":
    fns = [d_046, d_047, d_048]
    for fn in fns:
        fn()
        print("wrote", fn.__name__)