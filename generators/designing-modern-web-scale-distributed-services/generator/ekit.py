#!/usr/bin/env python3
"""Thin shim: shared drawing kit lives in generators/common (SSOT)."""
import os, sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, "..", ".."))   # generators/
sys.path.insert(0, os.path.join(_HERE, "..", "..", ".."))  # repo root

OUT = os.path.join(_HERE, "..", "generated")

import common.kit as _kit
_kit.OUT = OUT
from common.kit import *
from common.kit import _id, _nonce


def __getattr__(name):
    import common.kit as _k
    return getattr(_k, name)
