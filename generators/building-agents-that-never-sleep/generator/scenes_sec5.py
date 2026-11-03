#!/usr/bin/env python3
"""
scenes_sec5.py — Section 5 "Waiting for Input" diagrams (lessons 030-035).

Rebuilt on the user's simplified library (scenes_lib) in the
scalable_application style: black sw2 strokes, white canvas, fontFamily 1,
16-24px text; orange only for badges/incidents.
Run:  python3 scenes_sec5.py   (writes *.excalidraw next to this file)
"""
from ekit import *
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "..", "common"))
# common on path above? ensure generators/common importable
from scenes_lib import (place, metrics, REF_BG, hdr, cap, rref, eref, panel,
                        BLACK, MID, ACC, GRAY, GREEN, WHITE, file_name)


def d_030():
    """Choosing to wait — the permission model."""
    new()
    hdr("Choosing to Wait", 60, 36)
    text("Pausing is a first-class capability — and for non-destructive moves, the agent decides freely.", 60, 76, size=15, color=MID, width=860)
    dashed_group(70, 150, 700, 330, "Outcomes that need time or a human — the agent may decide freely")
    for i, (label, why) in enumerate([
        ("wait", "the world will change on its own\n(dependency recovers in 30s)"),
        ("ask for help", "only a human can change the world\n(upstream is gone for good)"),
        ("done (unmet goal)", "the agent wants to quit — the harness\nrejects it, see lesson 31"),
    ]):
        box(110, 200 + i * 92, 260, 76, label, size=14, fill=WHITE, stroke=BDR)
        text(why, 390, 238 + i * 92, size=12, color=MID, width=340)
    dashed_group(830, 150, 560, 330, "Anything destructive — the harness decides")
    box(870, 230, 480, 90, "rollback / release\n→ approval policy (Section 6)", size=13, fill=CON, stroke=ACC)
    text("never left to the model:\n\"rollback takes too long,\nso I'll do something else\"", 1110, 390, size=12, color=MID, align="center", width=440)
    text("pause = free compute: the run suspends and burns nothing while it waits", 320, 560, size=12, color=MID, align="center", width=700)
    save(file_name(30)[:-5], bg=REF_BG)


def d_031():
    """Suspending a run."""
    new()
    hdr("Suspending a Run", 60, 36)
    text("One guard, one write: the run parks itself with a reason — and waits to be woken.", 60, 76, size=15, color=MID, width=820)
    box(80, 200, 260, 120, "decision\naction", size=13, fill=WHITE, stroke=BLACK)
    text("wait", 210, 140, size=12, color=MID, align="center", anchor="ct")
    arrow(340, 260, 460, 260, color=ACC, w=3)
    acc_box(460, 170, 340, 180, "suspend guard\nwait | request help |\ncomplete-but-unmet", size=13)
    arrow(800, 260, 920, 260, color=BLACK, w=2)
    box(920, 190, 400, 130, "step \"wait-status\"\nsetRun({ status: \"waiting\", reason })", size=13, fill=WHITE, stroke=BLACK)
    text("running → waiting · reason per mode", 1120, 360, size=12, color=MID, align="center", width=360)
    box(920, 420, 400, 110, "", fill=CON, stroke=BDR)
    text("reject-completion:\n\"completion blocked by configured goal condition\"\n— deterministic override, not a human verdict", 1120, 465, size=12, align="center", anchor="ct", color=BLACK, width=360)
    arrow(800, 300, 920, 470, color=BLACK, w=2, dash=True)
    text("terminal statuses: completed · failed · cancelled · escalated · superseded", 460, 640, size=12, color=MID, align="center", width=700)
    save(file_name(31)[:-5], bg=REF_BG)


def d_032():
    """step.waitForEvent — wait by event, not by clock."""
    new()
    hdr("step.waitForEvent", 60, 36)
    text("Wake on the event — not on a poll that might miss it or burn hours.", 60, 76, size=15, color=MID, width=860)
    dashed_group(60, 150, 640, 430, "Option A — poll on a clock")
    text("step.sleep(60s) then query the event store…", 380, 200, size=13, color=BLACK, align="center", width=540)
    text("event arrives at second 3 → you wait 57 more,\nor poll faster and pay for it — imagine a 30-minute wait", 380, 260, size=12, color=MID, align="center", width=540)
    text("query at fixed intervals —\ncoarse, wasteful, wrong-paced", 380, 390, size=12, color=MID, align="center", width=520)
    dashed_group(760, 150, 620, 430, "Option B — waitForEvent")
    acc_box(800, 200, 540, 130, "step.waitForEvent(\"check\", {\n  event: \"incident/updated\",\n  if: \"async.data.runId === \" + runId,\n  timeout: \"10 seconds\"\n})", size=13)
    text("event arrives → workflow re-runs → cached\nsteps resume exactly at the wait (memoization)", 1070, 400, size=12, color=MID, align="center", width=500)
    text("serverless: function froze, compute zero · local: while-loop simulates the freeze", 700, 640, size=12, color=MID, align="center", width=680)
    save(file_name(32)[:-5], bg=REF_BG)


def d_033():
    """The wait loop."""
    new()
    hdr("The Wait Loop", 60, 36)
    text("While nothing has changed, the run idles in a bounded loop named by cycle and check.", 60, 76, size=15, color=MID, width=860)
    acc_box(110, 170, 420, 90, "while (true) {", size=15)
    arrow(530, 215, 620, 215, color=ACC, w=3)
    box(620, 170, 430, 90, "step.run(`read-events ${cycle}-${check}`)", size=14, fill=WHITE, stroke=BLACK)
    arrow(1050, 215, 1140, 215, color=BLACK, w=2)
    box(1140, 170, 280, 90, "new events?\nlatest.eventSequence\n> state.eventSequence", size=12, fill=WHITE, stroke=BDR)
    arrow(1140, 300, 700, 330, color=GREEN, w=3, start="arrow")
    text("yes → break the while →\ncontinue the outer for-loop → re-observe", 620, 340, size=12, color=MID, width=300)
    arrow(1370, 260, 1370, 380, color=BLACK, w=2)
    box(1140, 380, 280, 90, "no → check++\nand keep waiting", size=12, fill=CON, stroke=BDR)
    text("step names embed cycle + check, so the dashboard reads:\nloop 2 › while check 1/2 · loop 2 › while check 2/2…", 700, 560, size=12, color=MID, align="center", width=660)
    text("0 ms recovery = stuck forever: a run with no help tool and no event never returns", 700, 610, size=12, color=ACC, align="center", width=660)
    save(file_name(33)[:-5], bg=REF_BG)


def d_034():
    """Wait or ask for help?"""
    new()
    hdr("Wait or Ask for Help?", 60, 36)
    text("Both pause the run. The difference is what will resolve them.", 60, 76, size=15, color=MID, width=760)
    box(100, 200, 320, 130, "wait", size=15, fill=WHITE, stroke=BLACK)
    text("the world needs TIME\nan event will arrive on its own\n(dependency recovers)", 100, 300, size=12, color=MID, align="center", anchor="ct", width=280)
    box(100, 400, 320, 130, "ask for help", size=15, fill=WHITE, stroke=ACC)
    text("the world needs a HUMAN\nno event will fix it\n(upstream gone for good)", 100, 500, size=12, color=MID, align="center", anchor="ct", width=280)
    box(560, 200, 360, 330, "", fill=CON, stroke=BDR)
    text("both are non-destructive —\nthe agent may choose them freely", 740, 250, size=13, color=BLACK, align="center", width=320)
    text("a help request is not a dead end:\nany relevant event re-renders the run\n(\"never mind, I don't need help\")", 740, 330, size=12, color=MID, align="center", width=320)
    text("not built yet → defer-help step parks\nthe question in the activity log", 740, 440, size=12, color=MID, align="center", width=320)
    text("the human's reply is an event that wakes the run —\nexactly the trigger model of incident/updated", 560, 620, size=12, color=MID, align="center", width=520)
    save(file_name(34)[:-5], bg=REF_BG)


def d_035():
    """One harness, many runs."""
    new()
    hdr("One Harness, Many Runs", 60, 36)
    text("One workflow function, thousands of concurrent runs — each with its own incident.", 60, 76, size=15, color=MID, width=860)
    acc_box(120, 150, 440, 90, "one workflow function\n(\"agent-workflow\")", size=15)
    for i, (label, extra) in enumerate([
        ("run #8842", "checkout degraded → cured"),
        ("run #8890", "payment gateway down → help"),
        ("run #9911", "release fault → approval"),
    ]):
        box(120 + i * 250, 300, 230, 120, label, size=13, fill=WHITE, stroke=BDR)
        text(extra, 235 + i * 250, 380, size=11, color=MID, align="center", width=200)
    arrow(340, 240, 235, 300, color=ACC, w=3)
    arrow(340, 240, 485, 300, color=ACC, w=3)
    arrow(340, 240, 735, 300, color=ACC, w=3)
    dashed_group(740, 460, 660, 140, "sorting events into runs")
    text("triage LLM in front: \"are these alerts the same root cause?\"\n→ yes: reuse the open run · no: start a new run", 1070, 500, size=12, color=MID, align="center", width=560)
    text("three runs investigating one root cause can't talk — none ever resolves", 1070, 555, size=12, color=BLACK, align="center", width=560)
    text("system prompt can be event data — same harness, different personas", 420, 640, size=12, color=MID, align="center", width=660)
    save(file_name(35)[:-5], bg=REF_BG)


if __name__ == "__main__":
    fns = [d_030, d_031, d_032, d_033, d_034, d_035]
    for fn in fns:
        fn()
        print("wrote", fn.__name__)