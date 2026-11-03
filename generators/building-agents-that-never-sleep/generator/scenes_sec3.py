#!/usr/bin/env python3
"""
scenes_sec3.py — Section 3 "Goals and the Loop" diagrams (lessons 012-021).

Rebuilt on the user's simplified library (scenes_lib) in the
scalable_application style: black sw2 strokes, white canvas, fontFamily 1,
16-24px text; orange only for badges/incidents.
Run:  python3 scenes_sec3.py   (writes *.excalidraw next to this file)
"""
from ekit import *
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "builders"))
from scenes_lib import (place, metrics, REF_BG, hdr, cap, rref, eref, panel,
                        BLACK, MID, ACC, GRAY, GREEN, WHITE, file_name)


def d_012():
    """The agent's world — world state, run state, history."""
    new()
    hdr("The Agent's World", 60, 36)
    text("Three kinds of state feed every decision: the world, the run, and the history.", 60, 76, size=15, color=MID, width=800)

    place("app_server", 100, 195, scale=1.6, retag={"Application\nserver": "Checkout\nService"})
    arrow(254, 268, 420, 268, color=ACC, w=3)
    text("getAgentState", 380, 248, size=12, color=MID, align="center", anchor="cb")
    box(420, 170, 330, 160, "", fill=WHITE, stroke=BLACK)
    text("world state", 585, 180, size=13, align="center", anchor="ct", color=BLACK)
    text("health: degraded\nerrorRate: 42.1\nfeatures: {express: on}", 585, 205, size=12, color=BLACK, align="center", anchor="ct", width=300)
    box(820, 170, 330, 130, "", fill=CON, stroke=BDR)
    text("run state", 985, 180, size=13, align="center", anchor="ct", color=BLACK)
    text("runId · status: running\ngoalCondition · cycle: 3", 985, 215, size=12, color=BLACK, align="center", anchor="ct", width=290)
    box(820, 330, 330, 130, "", fill=CON, stroke=BDR)
    text("execution history", 985, 340, size=13, align="center", anchor="ct", color=BLACK)
    text("observed states, decisions,\nactions — everything so far", 985, 375, size=12, color=BLACK, align="center", anchor="ct", width=290)
    arrow(750, 250, 820, 250, color=BLACK, w=2)
    arrow(585, 340, 585, 560, color=BLACK, w=2)
    box(420, 560, 330, 70, "goal + state + history → each decision", size=13, fill=ACC, stroke=ACC, color=WHITE)
    text("the agent never decides what it observes — the harness force-feeds the world", 985, 660, size=12, color=MID, align="center", anchor="ct", width=460)
    save(file_name(12)[:-5], bg=REF_BG)


def d_013():
    """The action set — small and closed."""
    new()
    hdr("The Action Set", 60, 36)
    text("Seven actions. No open-ended tool bag.", 60, 76, size=15, color=MID, width=600)
    dashed_group(80, 150, 420, 480, "Read")
    for i, a in enumerate(["inspect logs", "inspect changes"]):
        rect(100, 200 + i * 90, 380, 70, fill=WHITE, stroke=BDR, rx=True)
        text(a, 290, 235 + i * 90, size=14, align="center", anchor="cm", color=BLACK)
    dashed_group(560, 150, 420, 480, "Write — guarded")
    for i, a in enumerate(["disable feature", "rollback / release"]):
        rect(580, 200 + i * 90, 380, 70, fill=WHITE, stroke=BDR, rx=True)
        text(a, 770, 235 + i * 90, size=14, align="center", anchor="cm", color=BLACK)
    text("writes can require approval\n(rollback → human, Section 6)", 770, 400, size=12, color=ACC, align="center", width=340)
    dashed_group(1040, 150, 400, 480, "Pause / terminal")
    for i, a in enumerate(["wait", "ask for help", "done"]):
        rect(1060, 200 + i * 90, 360, 70, fill=WHITE, stroke=BDR, rx=True)
        text(a, 1240, 235 + i * 90, size=14, align="center", anchor="cm", color=BLACK)
    text("closed set = easy to validate,\naudit, and keep approval-safe", 140, 690, size=12, color=MID, width=460)
    save(file_name(13)[:-5], bg=REF_BG)


def d_014():
    """The workflow function — event trigger + one step."""
    new()
    hdr("The Workflow Function", 60, 36)
    text("An Ingest function: an event in, a durable step, a report out.", 60, 76, size=15, color=MID, width=700)
    badge(140, 250, 1, r=20, fill=ACC)
    text("incident/opened", 140, 296, size=13, align="center", anchor="ct", color=BLACK)
    arrow(200, 265, 320, 265, color=ACC, w=3)
    box(320, 200, 300, 130, "createFunction\n\"agent-workflow\"", size=14, fill=WHITE, stroke=BLACK)
    text("event-driven — fire and forget", 470, 356, size=12, color=MID, align="center", anchor="ct")
    arrow(620, 265, 720, 265, color=BLACK, w=2)
    acc_box(720, 200, 340, 130, "step.run(\"whole agent loop\")", size=14)
    text("a step is a checkpoint —\nresults are memoized", 890, 356, size=12, color=MID, align="center", anchor="ct", width=320)
    arrow(1060, 250, 1160, 220, color=BLACK, w=2)
    box(1160, 190, 240, 90, "writeReport\n+ complete", size=13, fill=CON, stroke=BDR)
    arrow(1060, 290, 1160, 330, color=BLACK, w=2)
    box(1160, 300, 240, 90, "getRun(runId)\nre-entry, dedupes", size=13, fill=CON, stroke=BDR)
    text("same runId = same run — events can't start duplicates", 460, 480, size=12, color=MID, width=520)
    save(file_name(14)[:-5], bg=REF_BG)


def d_015():
    """Observing the world."""
    new()
    hdr("Observing the World", 60, 36)
    text("Every loop starts by reading the world. The agent is never allowed to skip it.", 60, 76, size=15, color=MID, width=760)
    place("app_server", 90, 200, scale=1.5, retag={"Application\nserver": "the world\n(checkout service)"})
    cap("the world", 169, 340, size=13)
    arrow(236, 270, 430, 270, color=ACC, w=3)
    text("getAgentState\n(environmentId, runId)", 350, 245, size=12, color=MID, align="center", anchor="cb", width=180)
    acc_box(430, 200, 300, 150, "observe state\n(step)", size=15)
    text("fresh snapshot,\nnever the agent's memory", 580, 310, size=12, color=MID, align="center", anchor="ct", width=280)
    arrow(730, 275, 840, 275, color=BLACK, w=2)
    box(840, 180, 300, 120, "state\nhealth · errorRate · features · version", size=13, fill=WHITE, stroke=BLACK)
    arrow(990, 300, 990, 380, color=BLACK, w=2)
    box(840, 380, 300, 130, "next: goal check\nthen decide", size=14, fill=CON, stroke=BDR)
    text("same shape as a screenshot for a browser agent —\na snapshot of the world at that instant", 200, 560, size=12, color=MID, width=560)
    save(file_name(15)[:-5], bg=REF_BG)


def d_016():
    """Deciding with the LLM."""
    new()
    hdr("Deciding with the LLM", 60, 36)
    text("One stateless call per loop: goal + state + history in, structured decision out.", 60, 76, size=15, color=MID, width=820)
    dashed_group(60, 160, 360, 400, "Inputs (every loop)")
    text("goalCondition", 240, 200, size=13, align="center", anchor="ct", color=BLACK)
    text("world state", 240, 260, size=13, align="center", anchor="ct", color=BLACK)
    text("history so far", 240, 320, size=13, align="center", anchor="ct", color=BLACK)
    arrow(420, 300, 530, 300, color=ACC, w=3)
    acc_box(530, 210, 320, 180, "", size=14)
    text("LLM", 690, 225, size=15, align="center", anchor="ct", color=BLACK)
    text("chooseAction(goal, state)\n\"reasoning function\"", 690, 255, size=12, align="center", anchor="ct", color=BLACK, width=300)
    arrow(850, 300, 960, 300, color=BLACK, w=2)
    box(960, 180, 380, 240, "", fill=WHITE, stroke=BLACK)
    text("structured output", 1150, 195, size=13, align="center", anchor="ct", color=BLACK)
    text("action: one of the 7", 1150, 230, size=12, align="center", anchor="ct", color=BLACK)
    text("reason: why now", 1150, 265, size=12, align="center", anchor="ct", color=BLACK)
    text("moreDetail: context", 1150, 300, size=12, align="center", anchor="ct", color=BLACK)
    text("AI SDK generateText + schema — the model cannot\nreturn anything that is not in the set", 640, 500, size=12, color=MID, align="center", width=560)
    save(file_name(16)[:-5], bg=REF_BG)


def d_017():
    """Acting on the world."""
    new()
    hdr("Acting on the World", 60, 36)
    text("The harness executes — with version checks and an audit record.", 60, 76, size=15, color=MID, width=800)
    box(80, 190, 260, 120, "decision\n{action, reason}", size=13, fill=WHITE, stroke=BLACK)
    arrow(340, 250, 440, 250, color=ACC, w=3)
    acc_box(440, 190, 300, 120, "executeAction\n(actionId, name)", size=13)
    arrow(740, 250, 840, 250, color=BLACK, w=2)
    place("app_server", 840, 180, scale=1.5, retag={"Application\nserver": "checkout\n/operations"})
    text("POST { actionId, name,\nexpectedVersion }", 970, 360, size=12, color=MID, align="center", width=300)
    arrow(969, 333, 969, 420, color=BLACK, w=2)
    box(840, 420, 260, 90, "stale? version drifted →\nre-observe, don't force it", size=12, fill=CON, stroke=BDR)
    arrow(400, 340, 260, 420, color=BLACK, dash=True, start="arrow")
    text("action must change observable state —\notherwise the agent loops blind", 220, 560, size=12, color=MID, width=440)
    arrow(620, 340, 620, 460, color=BLACK, w=2, dash=True)
    box(520, 460, 320, 80, "recordToolAction → Activities", size=13, fill=CON, stroke=BDR)
    save(file_name(17)[:-5], bg=REF_BG)


def d_018():
    """The loop and its guardrails."""
    new()
    hdr("The Loop and Its Guardrails", 60, 36)
    text("A bounded for-loop is the simplest safety mechanism in the system.", 60, 76, size=15, color=MID, width=680)
    acc_box(110, 150, 340, 80, "for (cycle = 0; cycle < 8; cycle++)", size=15)
    text("bounded, deterministic — no\nMath.random-flavored control flow", 280, 258, size=12, color=MID, align="center", width=320)
    arrow(450, 190, 540, 190, color=ACC, w=3)
    dashed_group(540, 130, 440, 420, "one loop body")
    box(560, 170, 170, 60, "observe state", size=12)
    box(780, 170, 180, 60, "goal met?", size=12)
    arrow(730, 200, 780, 200, color=BLACK, w=2)
    arrow(870, 230, 870, 280, color=BLACK, w=2)
    box(780, 280, 180, 60, "decide", size=12)
    arrow(870, 340, 870, 390, color=BLACK, w=2)
    box(780, 390, 180, 60, "act", size=12)
    arrow(870, 450, 870, 480, color=BLACK, w=2)
    text("cycle++", 900, 500, size=12, color=MID)
    arrow(340, 520, 740, 520, color=BLACK, w=2, dash=True)
    box(140, 520, 560, 70, "goal met → writeReport + complete run (exit)", size=13, fill=GREEN, stroke=GREEN, color=WHITE)
    arrow(120, 420, 120, 490, color=ACC, w=2, dash=True)
    text("8 attempts max — then the\nrun fails loudly, never loops forever", 140, 600, size=12, color=MID, width=560)
    save(file_name(18)[:-5], bg=REF_BG)


def d_019():
    """Deterministic goal checks."""
    new()
    hdr("Deterministic Goal Checks", 60, 36)
    text("Whether the goal is met is a code question — not a model opinion.", 60, 76, size=15, color=MID, width=780)
    box(80, 210, 240, 110, "state\n+ goalCondition", size=13, fill=WHITE, stroke=BLACK)
    acc_box(420, 200, 260, 130, "goalSatisfied()\ndeterministic compare", size=14)
    arrow(320, 260, 420, 260, color=ACC, w=3)
    text("pure object check —\nno tokens spent", 550, 360, size=12, color=MID, align="center", width=280)
    arrow(680, 240, 800, 200, color=GREEN, w=3)
    box(800, 150, 400, 110, "writeReport + updateRun(completed)\n→ return: the agent is done", size=13, fill=GREEN, stroke=GREEN, color=WHITE)
    arrow(680, 290, 800, 340, color=BLACK, w=2)
    box(800, 320, 400, 90, "else → decide next action\n(only now does the LLM run)", size=13, fill=CON, stroke=BDR)
    text("need judgment to know \"good\"? swap this for an LLM call\nevaluated against evals — the seam is one function", 260, 520, size=12, color=MID, align="center", width=620)
    save(file_name(19)[:-5], bg=REF_BG)


def d_020():
    """Keeping an audit trail."""
    new()
    hdr("Keeping an Audit Trail", 60, 36)
    text("An unattended agent must leave a perfect paper trail — there is no chat to scroll.", 60, 76, size=15, color=MID, width=820)
    for i, (n, label) in enumerate([("recordDecision", "action + reason"), ("recordToolAction", "actionId + result"), ("setIteration", "which cycle")]):
        box(110, 170 + i * 110, 330, 80, f"{n}\n({label})", size=13, fill=WHITE, stroke=BLACK)
        arrow(440, 210 + i * 110, 540, 210 + i * 110, color=ACC, w=3)
    browser(540, 150, 420, 420, "", size=14)
    text("Activities", 750, 165, size=12, align="center", anchor="ct", color=BLACK)
    for i, row in enumerate(["#3 observe state", "#3 decide: inspect logs (42.1%)", "#3 tool: inspect changes", "#2 disable feature", "goal satisfied"]):
        rect(560, 200 + i * 62, 380, 50, fill=WHITE, stroke=BDR, rx=True)
        text(row, 750, 225 + i * 62, size=11, align="center", anchor="cm", color=BLACK)
    text("every decision and action is recorded,\nwith its reasoning, before anything else happens", 750, 620, size=12, color=MID, align="center", width=460)
    save(file_name(20)[:-5], bg=REF_BG)


def d_021():
    """Workshop Q&A — goals and the loop."""
    new()
    hdr("Workshop Q&A: Goals and the Loop", 60, 36)
    text("The questions that shape how you think about the harness.", 60, 76, size=15, color=MID, width=800)
    dashed_group(70, 160, 620, 400, "Can a cheap model decide?")
    box(120, 230, 240, 100, "big model\nstructured output", size=12, fill=CON, stroke=BDR)
    box(420, 230, 240, 100, "tiny classifier\n(\"Jeff\" / \"Kev\")", size=12, fill=ACC, stroke=ACC, color=WHITE)
    text("works for picking an action — if the arguments\nit must produce are deterministic. Real answer:\nre-architect, then eval cost vs speed.", 405, 420, size=12, color=MID, align="center", width=560)
    dashed_group(760, 160, 660, 400, "SDK tool loop vs your loop?")
    text("the AI SDK's built-in loop re-runs tools until the\nmodel answers. \"wait\" and \"ask for help\" must\nintercept execution — pause, humans — so you\nbreak out and own the loop.", 1090, 240, size=12, color=MID, align="center", width=580)
    text("LLM single-shot; harness is the loop", 1090, 420, size=13, color=BLACK, align="center", width=560)
    text("same model + different harness = different agent", 300, 660, size=13, color=BLACK, align="center", width=560)
    save(file_name(21)[:-5], bg=REF_BG)


if __name__ == "__main__":
    fns = [d_012, d_013, d_014, d_015, d_016, d_017, d_018, d_019, d_020, d_021]
    for fn in fns:
        fn()
        print("wrote", fn.__name__)