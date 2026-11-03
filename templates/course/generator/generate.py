#!/usr/bin/env python3
"""Generate starter Excalidraw scene for {{COURSE_NAME}}."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from ekit import *

new()
title("{{COURSE_NAME}}", 60, 40)
subtitle("Starter scene - replace with your own diagrams.", 60, 80, width=700)
box(60, 140, 220, 90, "Input")
box(360, 140, 220, 90, "Process")
box(660, 140, 220, 90, "Output")
arrow(280, 185, 360, 185)
arrow(580, 185, 660, 185)
save("001 Starter")
