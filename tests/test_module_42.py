"""Tests for test module 42 — covers src modules [165, 166, 167, 168]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_165 import modulo_165
from module_166 import power_166
from module_167 import min_167
from module_168 import max_168

def test_modulo_165():
    assert modulo_165(10, 3) == 1

def test_power_166():
    assert power_166(2, 8) == 256

def test_min_167():
    assert min_167(3, 7) == 3

def test_max_168():
    assert max_168(3, 7) == 7
