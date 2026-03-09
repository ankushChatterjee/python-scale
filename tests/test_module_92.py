"""Tests for test module 92 — covers src modules [365, 366, 367, 368]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_365 import modulo_365
from module_366 import power_366
from module_367 import min_367
from module_368 import max_368

def test_modulo_365():
    assert modulo_365(10, 3) == 1

def test_power_366():
    assert power_366(2, 8) == 256

def test_min_367():
    assert min_367(3, 7) == 3

def test_max_368():
    assert max_368(3, 7) == 7
