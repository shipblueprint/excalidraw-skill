#!/usr/bin/env python3
"""Generate a starter Excalidraw scene for Prompt Test Course."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from ekit import *

new()
title("Prompt Test Course", 60, 40)
subtitle("Starter scene: sample layout of what you will build—a prompt test harness "
"for prompts, inputs, model outputs, assertions, and results.", 60, 82, width=900)
dashed_group(60, 150, 1180, 500, "Prompt Test Harness (sample layout)")

acc_box(90, 200, 260, 120, "Prompt Template\nsystem + user prompt")
box(90, 360, 260, 120, "Test Inputs\nvariables / cases")
box(400, 200, 240, 120, "Runner\nexecute prompt")
box(400, 360, 240, 120, "Model Output\ncaptured response")
box(690, 200, 260, 120, "Expected Output\nassertions")
box(690, 360, 260, 120, "Results\npass / fail")

arrow(350, 260, 400, 260)
text("prompt", 375, 248, size=11, color=MID, align="center", anchor="cb")
arrow(350, 420, 400, 420)
text("cases", 375, 408, size=11, color=MID, align="center", anchor="cb")
arrow_down(520, 320, 40)
text("run", 532, 335, size=11, color=MID, align="left", anchor="lm")
arrow(640, 420, 690, 420)
text("compare", 665, 408, size=11, color=MID, align="center", anchor="cb")
arrow_down(820, 320, 40)
text("expected", 832, 335, size=11, color=MID, align="left", anchor="lm")

text("Students will replace each box with working prompt-testing code.",
     90, 590, size=13, color=ACC)
credit()
save("001 Starter")
print("Wrote starter scene to generated/001 Starter.excalidraw")