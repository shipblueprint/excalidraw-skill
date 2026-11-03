#!/usr/bin/env python3
"""
scenes_sec6.py — Section 6 "Human in the Loop" diagrams (lessons 036-041).

Rebuilt on the user's simplified library (scenes_lib) in the
scalable_application style: black sw2 strokes, white canvas, fontFamily 1,
16-24px text; orange only for badges/incidents.
Run:  python3 scenes_sec6.py   (writes *.excalidraw next to this file)
"""
from ekit import *
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "builders"))
from scenes_lib import (place, metrics, REF_BG, hdr, cap, rref, eref, panel,
                        BLACK, MID, ACC, GRAY, GREEN, WHITE, file_name)


def _person(comp, x, y, label, scale=1.0):
    place(comp, x, y, scale=scale, retag={"User": label, "Node": ""})


def d_036():
    """Why an inbox, not a chat."""
    new()
    hdr("Why an Inbox, Not a Chat", 60, 36)
    text("The agent doesn't live in a conversation — it drops tasks you unblock, then waits on an event.", 60, 76, size=15, color=MID, width=880)
    dashed_group(60, 150, 620, 430, "chat — a conversation you babysit")
    browser(80, 195, 580, 300, "", size=14)
    for i, (who, msg) in enumerate([("you", "what happened?"), ("agent", "checkout is degraded…"),
                                    ("you", "ok, fix it"), ("agent", "on it — disable express")]):
        x = 100 if who == "you" else 360
        rect(x, 225 + i * 62, 280, 52, fill=CON if who == "you" else WHITE, stroke=BDR, rx=True)
        text(f"{who}: {msg}", x + 10, 251 + i * 62, size=11, anchor="lt", color=BLACK, width=250)
    text("the agent waits inside a thread;\nyou are effectively on call", 430, 590, size=12, color=MID, align="center", width=420)
    dashed_group(740, 150, 620, 430, "inbox — a task list you clear")
    browser(760, 195, 580, 300, "", size=14)
    rect(780, 230, 540, 110, fill=WHITE, stroke=ACC, rx=True)
    text("✓ rollback release v2", 800, 250, size=14, color=BLACK, width=400)
    text("pending your approval — the agent is blocked", 800, 285, size=12, color=MID, width=400)
    rect(780, 355, 540, 100, fill=WHITE, stroke=ACC, rx=True)
    text("? payment gateway is down", 800, 375, size=14, color=BLACK, width=400)
    text("needs an answer — could not proceed safely", 800, 410, size=12, color=MID, width=400)
    text("you clear tasks when you want;\nthe agent waits on an event, not a chat", 1240, 590, size=12, color=MID, align="center", width=520)
    _person("you", 1230, 620, "you", scale=0.7)
    save(file_name(36)[:-5], bg=REF_BG)


def d_037():
    """Which actions need approval."""
    new()
    hdr("Which Actions Need Approval", 60, 36)
    text("Approval lives in the action-policy mapping, not in the model's judgment.", 60, 76, size=15, color=MID, width=820)
    for i, (action, policy, gate) in enumerate([
        ("inspect logs", "read", "runs freely"),
        ("inspect changes", "read", "runs freely"),
        ("disable feature", "write", "may gate later"),
        ("rollback / release", "approval", "always gated"),
    ]):
        box(100, 170 + i * 90, 340, 70, action, size=13, fill=WHITE, stroke=BDR)
        box(500, 170 + i * 90, 300, 70, policy, size=13, fill=CON, stroke=BDR)
        box(860, 170 + i * 90, 400, 70, gate, size=13, fill=ACC if i == 3 else CON, stroke=ACC if i == 3 else BDR, color=BLACK)
        arrow(440, 205 + i * 90, 500, 205 + i * 90, color=BLACK, w=2)
        arrow(800, 205 + i * 90, 860, 205 + i * 90, color=BLACK, w=2)
    text("the model proposes a rollback; the harness intercepts it —\nthe model can't negotiate its way past a mapping", 200, 620, size=12, color=MID, align="center", width=760)
    text("de-risk the rest, so you approve 5 requests a day — not 20:\nrollback mechanisms · small blast radius · percentage rollouts", 200, 660, size=12, color=MID, align="center", width=760)
    save(file_name(37)[:-5], bg=REF_BG)


def d_038():
    """Proposing an action."""
    new()
    hdr("Proposing an Action", 60, 36)
    text("The harness writes the proposal with the observed version — then reads it back from the DB.", 60, 76, size=15, color=MID, width=860)
    box(80, 210, 280, 120, "decision\n\"rollback release\"\npolicy: approval", size=12, fill=WHITE, stroke=BLACK)
    arrow(360, 270, 460, 270, color=ACC, w=3)
    acc_box(460, 200, 360, 140, "step \"propose action\"\nproposeAction(environmentId,\n  runId, actionId, action,\n  { expectedVersion })", size=13)
    arrow(820, 270, 920, 240, color=BLACK, w=2)
    database(920, 180, 340, 160, "proposals\nstatus: pending\nexpectedVersion: v1", size=13)
    arrow(920, 340, 760, 420, color=BLACK, w=2)
    browser(600, 420, 420, 200, "", size=13)
    rect(620, 455, 380, 70, fill=WHITE, stroke=ACC, rx=True)
    text("✓ rollback release v2", 640, 475, size=13, color=BLACK, width=320)
    text("please review the exact action before I proceed", 640, 502, size=11, color=MID, width=320)
    text("expectedVersion comes from the world snapshot —\nevery state change bumps it, so the proposal\nfreezes the world the action was decided against", 1100, 300, size=12, color=MID, align="center", width=340)
    text("read it back from the DB (getProposal) — never reuse the\njust-created object: async writes + conflicts = stale reads", 1090, 450, size=12, color=MID, align="center", width=340)
    save(file_name(38)[:-5], bg=REF_BG)


def d_039():
    """Waiting and reconciling."""
    new()
    hdr("Waiting and Reconciling", 60, 36)
    text("Wait on the decision event, re-read the proposal, then make sure the world still matches.", 60, 76, size=15, color=MID, width=880)
    box(80, 200, 300, 120, "proposal\nstatus: pending", size=13, fill=WHITE, stroke=BLACK)
    arrow(380, 260, 480, 260, color=ACC, w=3)
    acc_box(480, 190, 380, 140, "step \"wait for human\"\nwaitForEvent → approval.decided\nif: async.data.proposalId", size=13)
    arrow(860, 260, 960, 260, color=BLACK, w=2)
    box(960, 200, 320, 120, "getProposal(proposalId)\nre-read every check", size=13, fill=WHITE, stroke=BLACK)
    arrow(1120, 320, 1120, 400, color=BLACK, w=2)
    text("pending → keep waiting (check++)", 1140, 360, size=12, color=MID)
    box(960, 400, 320, 100, "approved?\nno → stop after human\n(lesson 40)", size=12, fill=CON, stroke=BDR)
    arrow(960, 450, 820, 500, color=GREEN, w=2, start="arrow")
    box(500, 500, 320, 120, "recheck approved state\nfresh.world.version\nvs expectedVersion", size=12, fill=WHITE, stroke=BLACK)
    arrow(500, 560, 320, 540, color=ACC, w=2, dash=True)
    text("mismatch → staleProposal → re-observe,\nre-propose if still right (lesson 40)", 220, 520, size=12, color=MID, align="center", width=280)
    arrow(820, 560, 960, 560, color=GREEN, w=3)
    box(960, 540, 320, 80, "execute action with\nexpectedVersion", size=12, fill=GREEN, stroke=GREEN, color=WHITE)
    text("approval is a version contract: it is valid only against the world it was written for", 300, 680, size=12, color=MID, align="center", width=760)
    save(file_name(39)[:-5], bg=REF_BG)


def d_040():
    """Stale proposals and rejections."""
    new()
    hdr("Stale Proposals and Rejections", 60, 36)
    text("Two ways a proposal stops being actionable — and what the harness does about each.", 60, 76, size=15, color=MID, width=860)
    dashed_group(70, 150, 620, 420, "rejected — the human said no")
    box(110, 220, 260, 90, "proposal.status\n≠ approved", size=13, fill=WHITE, stroke=BLACK)
    arrow(370, 265, 450, 265, color=ACC, w=3)
    box(450, 200, 220, 90, "step \"stop after human\"", size=12, fill=CON, stroke=BDR)
    arrow(670, 245, 750, 245, color=BLACK, w=2)
    box(750, 180, 260, 90, "setRun → escalated\n(terminal status)", size=12, fill=ACC, stroke=ACC, color=WHITE)
    text("the run ends: the human decided;\na live run would be a lie", 360, 520, size=12, color=MID, align="center", width=520)
    dashed_group(760, 150, 620, 420, "stale — the world moved first")
    box(800, 220, 280, 90, "version drifted since\nthe proposal was made", size=12, fill=WHITE, stroke=BLACK)
    arrow(1080, 265, 1160, 265, color=ACC, w=3)
    box(1160, 200, 200, 90, "invalidate\napproval", size=13, fill=CON, stroke=BDR)
    text("staleProposal() → cleared\nfrom the inbox", 1260, 330, size=12, color=MID, align="center", width=180)
    arrow(1260, 290, 1260, 400, color=BLACK, w=2)
    box(800, 400, 560, 90, "continue the loop → re-observe →\nre-propose if the action is still right", size=12, fill=GREEN, stroke=GREEN, color=WHITE)
    text("overdraft analogy: you approve a transfer, then the balance\nchanges — the approval must be re-checked against reality", 1090, 560, size=12, color=MID, align="center", width=520)
    save(file_name(40)[:-5], bg=REF_BG)


def d_041():
    """Demo: approving a rollback."""
    new()
    hdr("Demo: Approving a Rollback", 60, 36)
    text("The full arc, with a human in the middle: propose → approve → execute → verify.", 60, 76, size=15, color=MID, width=900)
    steps = [
        ("incident\nopened", CON, BDR),
        ("observe\n(42.1%)", CON, BDR),
        ("decide:\nrollback release", CON, BDR),
        ("propose\n+ inbox", ACC, ACC),
        ("human\napproves", ACC, ACC),
        ("execute\nrollback → v2", CON, BDR),
        ("recovery +\nre-observe", CON, BDR),
        ("healthy →\nreport", GREEN, GREEN),
    ]
    _person("you", 700, 60, "you", scale=0.6)
    x = 40
    for i, (label, fill, stroke) in enumerate(steps):
        box(x, 200, 132, 110, label, size=11, fill=fill, stroke=stroke)
        if i < len(steps) - 1:
            arrow(x + 132, 255, x + 163, 255, color=BLACK, w=2)
        x += 163
    text("Approve clicked → fires agent/approval.decided → the workflow re-runs and\nresumes exactly at the wait — the proposal is re-read from the DB and rechecked", 350, 400, size=12, color=MID, align="center", width=760)
    box(350, 470, 760, 90, "rollback mutates state to version 2 · release V2-bad · service degraded →\nrecovery event → observe healthy → goal met → report written", size=12, fill=WHITE, stroke=BLACK)
    text("the agent proposed; the harness disposed — enforcement, audit, and human arbitration all in one arc", 350, 620, size=12, color=MID, align="center", width=760)
    save(file_name(41)[:-5], bg=REF_BG)


if __name__ == "__main__":
    fns = [d_036, d_037, d_038, d_039, d_040, d_041]
    for fn in fns:
        fn()
        print("wrote", fn.__name__)