"""Tests for test module 292 — covers src modules [1165, 1166, 1167, 1168]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1165 import modulo_1165
from module_1166 import power_1166
from module_1167 import min_1167
from module_1168 import max_1168

def test_modulo_1165():
    assert modulo_1165(10, 3) == 1

def test_power_1166():
    assert power_1166(2, 8) == 256

def test_min_1167():
    assert min_1167(3, 7) == 3

def test_max_1168():
    assert max_1168(3, 7) == 7
