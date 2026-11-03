"""Shim: SSOT moved to generators/common/style.py."""
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, ".."))          # generators/
sys.path.insert(0, os.path.join(_HERE, "..", ".."))    # repo root
from common.style import *
