"""Tests for test module 1292 — covers src modules [5165, 5166, 5167, 5168]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5165 import modulo_5165
from module_5166 import power_5166
from module_5167 import min_5167
from module_5168 import max_5168

def test_modulo_5165():
    assert modulo_5165(10, 3) == 1

def test_power_5166():
    assert power_5166(2, 8) == 256

def test_min_5167():
    assert min_5167(3, 7) == 3

def test_max_5168():
    assert max_5168(3, 7) == 7
