#!/usr/bin/env python3
"""Generate a starter Excalidraw scene for {{COURSE_NAME}}."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from ekit import *

new()
title("{{COURSE_NAME}}", 60, 40)
subtitle("Starter scene generated from the shared brand kit.", 60, 82, width=520)
box(60, 150, 220, 90, "Concept")
box(360, 150, 220, 90, "Diagram")
arrow(280, 195, 360, 195)
save("001 Starter")
print("Wrote starter scene to generated/001 Starter.excalidraw")
