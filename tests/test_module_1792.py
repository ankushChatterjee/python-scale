"""Tests for test module 1792 — covers src modules [7165, 7166, 7167, 7168]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7165 import modulo_7165
from module_7166 import power_7166
from module_7167 import min_7167
from module_7168 import max_7168

def test_modulo_7165():
    assert modulo_7165(10, 3) == 1

def test_power_7166():
    assert power_7166(2, 8) == 256

def test_min_7167():
    assert min_7167(3, 7) == 3

def test_max_7168():
    assert max_7168(3, 7) == 7
