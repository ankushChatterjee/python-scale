"""Tests for test module 792 — covers src modules [3165, 3166, 3167, 3168]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3165 import modulo_3165
from module_3166 import power_3166
from module_3167 import min_3167
from module_3168 import max_3168

def test_modulo_3165():
    assert modulo_3165(10, 3) == 1

def test_power_3166():
    assert power_3166(2, 8) == 256

def test_min_3167():
    assert min_3167(3, 7) == 3

def test_max_3168():
    assert max_3168(3, 7) == 7
