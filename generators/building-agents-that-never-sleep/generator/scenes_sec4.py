#!/usr/bin/env python3
"""
scenes_sec4.py — Section 4 "The Durable Loop" diagrams (lessons 022-029).

Rebuilt on the user's simplified library (scenes_lib) in the
scalable_application style: black sw2 strokes, white canvas, fontFamily 1,
16-24px text; orange only for badges/incidents.
Run:  python3 scenes_sec4.py   (writes *.excalidraw next to this file)
"""
from ekit import *
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "..", "common"))
# common on path above? ensure generators/common importable
from scenes_lib import (place, metrics, REF_BG, hdr, cap, rref, eref, panel,
                        BLACK, MID, ACC, GRAY, GREEN, WHITE, file_name)


def d_022():
    """The one-step problem — crash replays everything."""
    new()
    hdr("The One-Step Problem", 60, 36)
    text("One giant step: a crash mid-run means starting the whole loop over.", 60, 76, size=15, color=MID, width=760)
    dashed_group(80, 150, 580, 420, "Before — one big step")
    acc_box(140, 200, 460, 140, "step.run(\"whole agent loop\")", size=14)
    text("observe · decide · act · act · decide…", 370, 380, size=12, color=MID, align="center", width=420)
    box(140, 430, 460, 70, "…becomes a wall of unknown progress —\nany crash means replaying from the start", size=12, fill=CON, stroke=BDR)
    dashed_group(740, 150, 660, 420, "After — named steps")
    steps = [("observe", 760), ("decide", 920), ("act", 1080), ("wait?", 1240)]
    for i, (s, x) in enumerate(steps):
        box(x, 200, 120, 60, s, size=12, fill=WHITE, stroke=BDR)
        if i < len(steps) - 1:
            arrow(x + 120, 230, x + 190, 230, color=BLACK, w=2)
    badge(760, 185, 1, r=13)
    badge(920, 185, 2, r=13)
    badge(1080, 185, 3, r=13)
    badge(1240, 185, 4, r=13)
    text("each step is its own checkpoint — a crashed run\nresumes from the last finished step", 1000, 460, size=12, color=MID, align="center", width=520)
    arrow(1240, 260, 1360, 300, color=GREEN, w=2)
    text("resume → skip\nfinished work", 1300, 340, size=11, color=MID, align="center", width=130)
    save(file_name(22)[:-5], bg=REF_BG)


def d_023():
    """Steps are checkpoints — memoization, not stack replay."""
    new()
    hdr("Steps Are Checkpoints", 60, 36)
    text("Durable execution is memoization — cached step results are rehydrated on replay.", 60, 76, size=15, color=MID, width=820)
    box(90, 180, 300, 110, "step.run(\"observe\", …)", size=13, fill=WHITE, stroke=BLACK)
    text("✓ result #1 cached", 240, 315, size=12, color=GREEN, align="center")
    box(430, 180, 300, 110, "step.run(\"decide\", …)", size=13, fill=WHITE, stroke=BLACK)
    text("✓ result #2 cached", 580, 315, size=12, color=GREEN, align="center")
    box(770, 180, 300, 110, "step.run(\"act\", …)", size=13, fill=WHITE, stroke=BLACK)
    text("✗ crashed while running — no cache yet", 920, 315, size=12, color=ACC, align="center", width=280)
    box(1110, 180, 260, 110, "step.run(\"wait\", …)", size=13, fill=CON, stroke=BDR)
    text("never reached", 1240, 315, size=12, color=MID, align="center")
    arrow(390, 235, 430, 235, color=BLACK, w=2)
    arrow(730, 235, 770, 235, color=BLACK, w=2)
    arrow(1070, 235, 1110, 235, color=BLACK, w=2)
    acc_box(430, 380, 640, 100, "replay: observe ✓ (memoized) · decide ✓ (memoized) · act → re-runs", size=14)
    text("not a stack replay — orchestration re-executes and\nmemoized step results come back from the cache", 420, 530, size=12, color=MID, align="center", width=640)
    save(file_name(23)[:-5], bg=REF_BG)


def d_024():
    """Determinism and idempotency."""
    new()
    hdr("Determinism and Idempotency", 60, 36)
    text("Two contracts keep replay safe: the workflow is deterministic, the steps are idempotent.", 60, 76, size=15, color=MID, width=860)
    dashed_group(70, 150, 640, 430, "Deterministic workflow")
    text("code between steps must not branch on\nrandom or time: replay must land in the\nsame place, every time", 390, 210, size=13, color=BLACK, align="center", width=440)
    box(120, 330, 220, 90, "Math.random()\nas a loop bound ✗", size=13, fill=CON, stroke=BDR)
    box(400, 330, 260, 90, "fixed for (0…24) ✓", size=13, fill=WHITE, stroke=GREEN)
    text("control-flow dependence is what matters —\na random id that nothing branches on is fine", 390, 480, size=12, color=MID, align="center", width=560)
    dashed_group(780, 150, 620, 430, "Idempotent steps")
    text("re-running a step must not repeat its effect\n(Stripe-style idempotency keys)", 1090, 210, size=13, color=BLACK, align="center", width=520)
    for i, r in enumerate(["charge(id=KEY) → 200 ✓", "charge(id=KEY) again → 200 ✓"]):
        box(820, 280 + i * 80, 540, 60, r, size=13, fill=WHITE, stroke=GREEN if i == 0 else BDR)
    text("same key, same response — no double charge", 1090, 470, size=12, color=MID, align="center", width=520)
    save(file_name(24)[:-5], bg=REF_BG)


def d_025():
    """Business state vs workflow state."""
    new()
    hdr("Business State vs Workflow State", 60, 36)
    text("Your database owns the truth; the workflow runtime owns checkpoints.", 60, 76, size=15, color=MID, width=820)
    box(90, 200, 360, 240, "", fill=WHITE, stroke=BLACK)
    text("your app database", 270, 215, size=14, align="center", anchor="ct", color=BLACK)
    text("runs · events · actions\nobservations · proposals\n(the business truth)", 270, 265, size=13, align="center", anchor="ct", color=BLACK, width=320)
    box(560, 200, 620, 240, "", fill=CON, stroke=BDR)
    text("workflow runtime (Ingest)", 870, 215, size=14, align="center", anchor="ct", color=BLACK)
    text("step results, memoized for replay\n(checkpoints — reconstruction data)", 870, 265, size=13, align="center", anchor="ct", color=BLACK, width=500)
    text("you never persist checkpoints yourself —\neach completed step auto-checkpoints", 870, 350, size=12, color=MID, align="center", width=560)
    box(90, 520, 1090, 110, "", fill=CON, stroke=BDR)
    text("versioning: deploy v2 while v1 runs die out — new runs get v2, in-flight v1 runs finish or are stopped; like migrating rows when a column changes", 635, 575, size=12, color=BLACK, align="center", width=1000)
    save(file_name(25)[:-5], bg=REF_BG)


def d_026():
    """Refactoring the loop."""
    new()
    hdr("Refactoring the Loop", 60, 36)
    text("Run validation first, then a bounded loop where every async thing is a step.", 60, 76, size=15, color=MID, width=860)
    box(90, 170, 300, 110, "guard: instanceId matches + run\nnot in {completed, failed, cancelled,\nescalated, superseded}", size=12, fill=WHITE, stroke=BLACK)
    arrow(390, 225, 470, 225, color=BLACK, w=2)
    acc_box(470, 170, 340, 110, "for (cycle = 1; cycle <= 24; cycle++)", size=15)
    text("loop lives in the workflow\n(a step would be memoized)", 640, 315, size=12, color=MID, align="center", width=330)
    arrow(810, 225, 900, 225, color=ACC, w=3)
    dashed_group(900, 150, 520, 420, "one iteration")
    for i, s in enumerate(["observe state", "goal check (outside steps)", "choose action", "set iteration", "record decision", "execute action"]):
        box(920, 180 + i * 56, 480, 44, s, size=12, fill=WHITE if i != 1 else CON, stroke=BDR)
        arrow(920, 224 + i * 56, 910, 224 + i * 56, color=BLACK, w=2)
    text("getRun(runId) at the top, deliberately\nNOT in a step — always current", 920, 560, size=11, color=MID, width=460)
    text("each step named with its cycle for observability", 920, 590, size=11, color=MID, width=460)
    save(file_name(26)[:-5], bg=REF_BG)


def d_027():
    """A step is a useMemo."""
    new()
    hdr("A Step Is a useMemo", 60, 36)
    text("The workflow is a component that re-renders on replay; steps are its memoized computations.", 60, 76, size=15, color=MID, width=860)
    dashed_group(80, 160, 330, 400, "replay re-renders")
    text("uncached top-level code reruns\non every replay — including\npaid, non-deterministic calls", 245, 220, size=13, color=BLACK, align="center", width=280)
    text("without a step, chooseAction\nwould re-run the LLM each replay:\ncost + latency + drift", 245, 340, size=12, color=MID, align="center", width=290)
    acc_box(500, 170, 700, 380, "", size=14)
    text("steps = useMemo", 850, 190, size=15, align="center", anchor="ct", color=BLACK)
    for i, s in enumerate(["observe state", "choose action (LLM — paid!)", "set iteration", "record decision", "execute action"]):
        box(530, 230 + i * 58, 640, 46, s, size=12, fill=WHITE, stroke=BDR)
        if i > 0:
            text("cached ✓", 1180, 253 + i * 58, size=11, color=GREEN, anchor="rt")
    line(500, 160, 500, 550, color=BLACK, w=2)
    save(file_name(27)[:-5], bg=REF_BG)


def d_028():
    """Action policies."""
    new()
    hdr("Action Policies", 60, 36)
    text("One branch per policy kind — not per action. Scales to thirty actions with six ifs.", 60, 76, size=15, color=MID, width=860)
    box(80, 200, 260, 120, "decision.action", size=14, fill=WHITE, stroke=BLACK)
    acc_box(420, 180, 260, 160, "actionPolicy(action)\n→ kind", size=15)
    arrow(340, 260, 420, 260, color=ACC, w=3)
    for i, (kind, example, branch) in enumerate([
        ("read", "inspect logs·changes", "run the step"),
        ("write", "disable·rollback", "maybe approval"),
        ("approval", "rollback", "inbox → human"),
    ]):
        box(760, 160 + i * 130, 580, 110, f"{kind}\n({example}) → {branch}", size=13, fill=CON if i != 2 else WHITE, stroke=ACC if i == 2 else BDR)
        arrow(680, 260, 760, 215 + i * 130, color=BLACK, w=2)
    text("add a 30th action tomorrow? you add a mapping row —\nnot another if-branch in the workflow", 400, 580, size=12, color=MID, align="center", width=640)
    save(file_name(28)[:-5], bg=REF_BG)


def d_029():
    """Demo — the agent fixes an outage."""
    new()
    hdr("Demo: The Agent Fixes an Outage", 60, 36)
    text("One incident, fully self-served: investigate, disable, verify, report.", 60, 76, size=15, color=MID, width=880)
    steps = [
        ("incident\nopened", ACC, ACC),
        ("observe\n(42.1%, express on)", CON, BDR),
        ("decide:\ninspect changes", CON, BDR),
        ("found: \"enabled\ncheckout express\"", CON, BDR),
        ("decide:\ndisable feature", CON, BDR),
        ("act:\ndisable express", CON, BDR),
        ("recover event\n→ re-observe", CON, BDR),
        ("goal met:\nhealthy, error 1%", GREEN, GREEN),
    ]
    x = 40
    for i, (label, fill, stroke) in enumerate(steps):
        box(x, 190, 132, 110, label, size=11, fill=fill, stroke=stroke)
        if i < len(steps) - 1:
            arrow(x + 132, 245, x + 163, 245, color=BLACK, w=2)
        x += 163
    badge(106, 172, 1, r=15, fill=ACC)
    text("the run self-verifies its own fix — the last loop observes\nhealthy state before writing the report", 300, 380, size=12, color=MID, align="center", width=660)
    box(300, 470, 660, 90, "writeReport + updateRun(completed)", size=14, fill=WHITE, stroke=BLACK)
    text("no prompts. one LLM call per cycle. guardrails and audit along the way.", 300, 610, size=12, color=MID, align="center", width=660)
    save(file_name(29)[:-5], bg=REF_BG)


if __name__ == "__main__":
    fns = [d_022, d_023, d_024, d_025, d_026, d_027, d_028, d_029]
    for fn in fns:
        fn()
        print("wrote", fn.__name__)