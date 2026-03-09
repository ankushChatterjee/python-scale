"""Tests for test module 1842 — covers src modules [7365, 7366, 7367, 7368]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7365 import modulo_7365
from module_7366 import power_7366
from module_7367 import min_7367
from module_7368 import max_7368

def test_modulo_7365():
    assert modulo_7365(10, 3) == 1

def test_power_7366():
    assert power_7366(2, 8) == 256

def test_min_7367():
    assert min_7367(3, 7) == 3

def test_max_7368():
    assert max_7368(3, 7) == 7
