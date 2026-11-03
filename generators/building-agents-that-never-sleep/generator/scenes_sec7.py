#!/usr/bin/env python3
"""
scenes_sec7.py — Section 7 "Safe Retries" diagrams (lessons 042-045).

Rebuilt on the user's simplified library (scenes_lib) in the
scalable_application style: black sw2 strokes, white canvas, fontFamily 1,
16-24px text; orange only for badges/incidents.
Run:  python3 scenes_sec7.py   (writes *.excalidraw next to this file)
"""
from ekit import *
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "..", "common"))
# common on path above? ensure generators/common importable
from scenes_lib import (place, metrics, REF_BG, hdr, cap, rref, eref, panel,
                        BLACK, MID, ACC, GRAY, GREEN, WHITE, file_name)


def d_042():
    """Idempotency keys for tool calls."""
    new()
    hdr("Idempotency Keys for Tool Calls", 60, 36)
    text("A retry must replay the same key — so the service recognizes it instead of repeating it.", 60, 76, size=15, color=MID, width=860)
    dashed_group(60, 150, 620, 430, "Stripe-style: the key makes a retry honest")
    for i, r in enumerate(["charge(id=KEY) → 200 ✓", "charge(id=KEY) again → 200 ✓", "one actual charge — ever"]):
        rect(90, 200 + i * 90, 560, 66, fill=WHITE, stroke=GREEN if i == 0 else BDR, rx=True)
        text(r, 370, 233 + i * 90, size=14, align="center", anchor="cm", color=BLACK)
    dashed_group(740, 150, 620, 430, "the action key becomes deterministic")
    acc_box(780, 200, 540, 120, "actionId = runId + cycle + action", size=14)
    text("derivable from what you already know —\nthe same retry recomputes the same key", 1050, 350, size=12, color=MID, align="center", width=500)
    box(780, 420, 540, 90, "the service dedupes on it:\nsame key, same response — no double rollback", size=13, fill=CON, stroke=BDR)
    text("random ids → retries become double-executions →\n\"the user already exists\" class of bugs", 250, 650, size=12, color=MID, align="center", width=620)
    save(file_name(42)[:-5], bg=REF_BG)


def d_043():
    """One run per incident."""
    new()
    hdr("One Run per Incident", 60, 36)
    text("Events are doorbells, not payloads — they ring once and the run answers once.", 60, 76, size=15, color=MID, width=860)
    dashed_group(60, 150, 620, 430, "doorbells, not payloads")
    for i, a in enumerate(["alert 1", "alert 2", "alert 3"]):
        badge(120 + i * 140, 210, i + 1, r=17, fill=ACC)
        text(a, 120 + i * 140, 245, size=12, align="center", anchor="ct", color=BLACK)
    arrow(420, 260, 540, 300, color=ACC, w=3)
    acc_box(540, 260, 120, 90, "one\nincident", size=14)
    text("three alerts attach to one incident → one run,\neach wake just re-reads the world state", 370, 480, size=12, color=MID, align="center", width=520)
    dashed_group(740, 150, 620, 430, "the re-entrancy guard")
    box(780, 200, 260, 110, "wake up → getRun(runId)", size=13, fill=WHITE, stroke=BLACK)
    box(1080, 200, 240, 110, "terminal status? → stop", size=13, fill=CON, stroke=BDR)
    arrow(1040, 255, 1080, 255, color=BLACK, w=2)
    text("completed · failed · cancelled ·\nescalated · superseded —\nthe state could have changed\nunderneath your feet", 1110, 380, size=12, color=MID, align="center", width=250)
    text("cancelOn(agent/run.cancelled) — one cursor per doc:\ntwo runs on the same runId is two people editing", 1060, 520, size=12, color=ACC, align="center", width=300)
    save(file_name(43)[:-5], bg=REF_BG)


def d_044():
    """Step retry semantics."""
    new()
    hdr("Step Retry Semantics", 60, 36)
    text("A step is the unit of retry — so a step must be one async, destructible thing.", 60, 76, size=15, color=MID, width=880)
    dashed_group(60, 150, 620, 440, "a fat step retries everything")
    box(100, 190, 540, 160, "", fill=WHITE, stroke=BDR)
    text("step \"create user\"", 370, 205, size=13, align="center", anchor="ct", color=BLACK)
    for i, ln in enumerate(["insert user", "send email", "charge card"]):
        text(f"{i+1}. {ln}", 120, 240 + i * 34, size=12, color=BLACK, width=200)
    text("crashes at 2/3 → the retry replays\n1 and 2 → \"user already exists\"", 370, 430, size=12, color=MID, align="center", width=520)
    dashed_group(740, 150, 620, 440, "tiny steps retry only the loser")
    for i, s in enumerate(["insert user", "send email", "charge card"]):
        box(780, 190 + i * 100, 260, 70, s, size=13, fill=WHITE, stroke=BDR)
        arrow(1040, 225 + i * 100, 1100, 225 + i * 100, color=BLACK, w=2)
        box(1100, 190 + i * 100, 180, 70, "own retry\npolicy", size=12, fill=CON, stroke=BDR)
    text("each step = separate retries for free;\none async destructible thing per step,\nand idempotent keys make even that safe", 1050, 560, size=12, color=MID, align="center", width=300)
    save(file_name(44)[:-5], bg=REF_BG)


def d_045():
    """Guardrails and budgets."""
    new()
    hdr("Guardrails and Budgets", 60, 36)
    text("Limits that live in code decide when a run must stop — not prose in a prompt.", 60, 76, size=15, color=MID, width=880)
    for i, (gate, what) in enumerate([
        ("for (cycle ≤ 24)", "a bounded loop can't run away"),
        ("decision limit", "decisionLimitReached → failed, loudly"),
        ("goal check first", "already-healthy runs spend 0 tokens"),
        ("terminal statuses", "completed · failed · escalated… → exit"),
    ]):
        box(90, 160 + i * 110, 380, 88, gate, size=15, fill=WHITE, stroke=BLACK)
        text(what, 90, 220 + i * 110, size=12, color=MID, width=360)
    acc_box(560, 180, 760, 160, "one LLM call per cycle · zero calls for goal checks\n→ cents per incident, not dollars", size=15)
    box(560, 400, 760, 150, "", fill=CON, stroke=BDR)
    text("budgets belong in the harness: deterministic, testable,\nnever negotiable by the model. \"please don't loop forever\"\nis a mood; cycle <= 24 is a guarantee", 940, 460, size=13, color=BLACK, align="center", width=660)
    text("a run that fails loudly is better than one that loops silently", 940, 620, size=12, color=MID, align="center", width=660)
    save(file_name(45)[:-5], bg=REF_BG)


if __name__ == "__main__":
    fns = [d_042, d_043, d_044, d_045]
    for fn in fns:
        fn()
        print("wrote", fn.__name__)