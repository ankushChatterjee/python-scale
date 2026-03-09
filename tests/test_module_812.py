"""Tests for test module 812 — covers src modules [3245, 3246, 3247, 3248]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3245 import modulo_3245
from module_3246 import power_3246
from module_3247 import min_3247
from module_3248 import max_3248

def test_modulo_3245():
    assert modulo_3245(10, 3) == 1

def test_power_3246():
    assert power_3246(2, 8) == 256

def test_min_3247():
    assert min_3247(3, 7) == 3

def test_max_3248():
    assert max_3248(3, 7) == 7
