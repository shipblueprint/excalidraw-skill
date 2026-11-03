#!/usr/bin/env python3
"""
scenes_sec1.py — Section 1 "Introduction" diagrams (lessons 001-005).

Rebuilt on the user's simplified library (scenes_lib) in the
scalable_application style: black sw2 strokes, white canvas, fontFamily 1,
16-24px text; orange only for badges/incidents.
Run:  python3 scenes_sec1.py   (writes *.excalidraw next to this file)
"""
from ekit import *
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "builders"))
from scenes_lib import (place, metrics, REF_BG, hdr, cap, rref, eref, panel,
                        BLACK, MID, ACC, GRAY, WHITE, file_name)


def _person(comp, x, y, label, scale=1.0):
    """Place a user/you person icon (visual top-left at x, y), re-labelled."""
    place(comp, x, y, scale=scale, retag={"User": label, "Node": ""})


def _device(x, y, label, scale=1.0):
    """Place the computer/terminal icon, re-labelled."""
    place("computer", x, y, scale=scale, retag={"Node": label})


def d_001():
    """Welcome — event -> agent -> dashboard, with the real components."""
    new()
    hdr("Welcome to the Course", 60, 36)
    text("You'll build a background agent that watches a service\nand fixes incidents — while you sleep.", 60, 76, size=15, color=MID, width=760)

    place("app_server", 90, 170, retag={"Application\nserver": "Checkout\nService"})
    cap("the fake service\nthat keeps breaking", 138, 280, size=13)

    badge(398, 217, 1, r=17)
    text("incident/opened", 424, 204, size=12, color=BLACK)
    arrow(186, 217, 368, 217, color=ACC, w=3)
    arrow(414, 217, 520, 217, color=ACC, w=3)

    rref(520, 160, 300, 145)
    text("Background Agent", 670, 192, size=18, align="center", anchor="ct", color=BLACK)
    cap("watches, pauses,\nwaits, resumes", 670, 272, size=13)

    arrow(820, 226, 950, 226, color=BLACK, w=2)
    _device(950, 168, "", scale=1.35)
    cap("the dashboard you'll build", 1000, 352, size=13)

    _person("user", 110, 500, "Customers")
    cap("customers keep buying", 155, 740, size=13)
    _person("you", 1240, 500, "You")
    cap("you — while you sleep", 1285, 740, size=13)
    save(file_name(1)[:-5], bg=REF_BG)


def d_002():
    """What is a background agent — event-driven, goal-directed, no prompting."""
    new()
    hdr("What Is a Background Agent?", 60, 36)
    text("Not a chat agent — work that happens without you asking for it.", 60, 76, size=15, color=MID, width=760)

    panel(60, 150, 540, 470, "Not a chat prompt")
    _person("user", 100, 225, "You")
    arrow(260, 320, 380, 320, dash=True, color=BLACK, w=2)
    cap("one-shot", 320, 300, size=13)
    cap("ask once, get one\nanswer, move on", 190, 480, size=13)
    cap("no instance running\nin the background", 210, 545, size=13)

    panel(700, 150, 680, 470, "A background agent")
    badge(780, 240, 1, r=16)
    text("event or change\n(e.g. incident opened)", 810, 228, size=13, color=BLACK)
    arrow(812, 247, 1020, 247, color=ACC, w=3)
    rref(1020, 190, 250, 120)
    text("Background Agent", 1145, 218, size=18, align="center", anchor="ct", color=BLACK)
    cap("observe → decide → act", 1145, 288, size=13)
    arrow(1145, 315, 1145, 365, color=BLACK, dash=True, w=2)
    _person("you", 1080, 380, "you", scale=0.9)
    cap("you — while you sleep", 1125, 602, size=13)
    cap("works until the goal is met —\nretries, waits, asks a human", 770, 355, size=13, width=210)
    save(file_name(2)[:-5], bg=REF_BG)


def d_003():
    """Goals, not prompts — why a goal gives an agent staying power."""
    new()
    hdr("Goals, Not Prompts", 60, 36)
    text("A prompt is a one-shot question. A goal is a target state the agent keeps working toward.", 60, 76, size=15, color=MID, width=860)

    panel(60, 150, 560, 470, "Chat prompt")
    _person("user", 100, 225, "User")
    arrow(260, 320, 380, 320, color=BLACK, w=2)
    text("Make a diagram\nof our API", 400, 300, size=14, color=BLACK, width=180)
    arrow(410, 375, 330, 425, color=BLACK, w=2)
    cap("one answer", 250, 438, size=13)
    cap("then it's done.\nNo one watching.", 300, 520, size=13)

    panel(700, 150, 640, 470, "Goal")
    rref(750, 220, 270, 100, fill=WHITE)
    text("Goal — \"restore checkout\"", 885, 232, size=15, align="center", anchor="ct", color=BLACK)
    cap("a target state the agent\nkeeps working toward", 885, 300, size=12)
    badge(1020, 240, 1, r=16)
    arrow(1026, 248, 1060, 248, color=ACC, w=3)
    for i, s in enumerate(["observe", "decide", "act"]):
        rref(1060 + i * 100, 220, 88, 54)
        text(s, 1104 + i * 100, 247, size=13, align="center", anchor="cm", color=BLACK)
    cap("keeps working: retries,\nwaits, asks a human", 810, 380, size=13, width=220)
    cap("stops only when the goal\ncondition is met", 1060, 480, size=13, width=220)
    save(file_name(3)[:-5], bg=REF_BG)


def d_004():
    """The authority problem — the LLM decides, the harness holds the authority."""
    new()
    hdr("The Authority Problem", 60, 36)
    text("Who decides what an unattended agent is allowed to do? Not the LLM.", 60, 76, size=15, color=MID, width=760)

    rref(80, 170, 360, 300)
    text("Agent (LLM)", 260, 186, size=16, align="center", anchor="ct", color=BLACK)
    for i, it in enumerate(["choose the next action", "reason about the world", "explain its decision"]):
        text("• " + it, 100, 235 + i * 34, size=13, color=BLACK, width=330)

    line(540, 150, 540, 500, color=MID, w=2, dash=True)

    rref(620, 170, 430, 300, fill=WHITE, stroke=ACC)
    text("Harness", 835, 186, size=16, align="center", anchor="ct", color=BLACK)
    for i, it in enumerate(["validates every action", "applies guardrails (loop limits)", "decides what needs approval", "executes or blocks the action", "keeps the audit trail"]):
        text("• " + it, 640, 235 + i * 34, size=13, color=BLACK, width=400)

    text("The LLM must never decide when\na decision needs a human approval", 835, 545, size=13, color=ACC, align="center", anchor="ct", width=420)
    text("the agent proposes — the harness disposes", 835, 610, size=12, color=MID, align="center", anchor="ct", width=380)
    save(file_name(4)[:-5], bg=REF_BG)


def d_005():
    """Anatomy of a background agent — LLM + harness."""
    new()
    hdr("Anatomy of a Background Agent", 60, 36)
    text("Agent = LLM + harness. The LLM is a reasoning function; the harness is everything else.", 60, 76, size=15, color=MID, width=880)

    panel(80, 150, 1180, 440, "The Agent")
    text("Harness", 130, 195, size=16, color=BLACK)
    for i, it in enumerate(["the Observe-Decide-Act loop", "world state, run state, history", "a small set of permitted actions", "guardrails and audit logging", "waiting and human approvals"]):
        text("• " + it, 100, 255 + i * 36, size=13, color=BLACK, width=520)

    rref(820, 220, 300, 150, fill=WHITE, stroke=ACC)
    text("LLM", 970, 236, size=16, align="center", anchor="ct", color=BLACK)
    text("reasoning function:\n\"given goal + state,\nwhat should I do?\"", 970, 268, size=12, align="center", anchor="ct", color=BLACK, width=260)

    arrow(700, 285, 820, 285, color=ACC, w=3)
    cap("~4 lines of code,\nthe cheapest part", 750, 258, size=11, width=170)

    _device(1080, 430, "", scale=1.0)
    cap("node process · any runner", 1118, 578, size=12)
    text("Same models, different harnesses —\nthat's why agents behave differently", 640, 640, size=13, color=MID, align="center", anchor="ct", width=460)
    save(file_name(5)[:-5], bg=REF_BG)


if __name__ == "__main__":
    for fn in (d_001, d_002, d_003, d_004, d_005):
        fn()
        print("wrote", fn.__name__)