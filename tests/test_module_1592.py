"""Tests for test module 1592 — covers src modules [6365, 6366, 6367, 6368]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6365 import modulo_6365
from module_6366 import power_6366
from module_6367 import min_6367
from module_6368 import max_6368

def test_modulo_6365():
    assert modulo_6365(10, 3) == 1

def test_power_6366():
    assert power_6366(2, 8) == 256

def test_min_6367():
    assert min_6367(3, 7) == 3

def test_max_6368():
    assert max_6368(3, 7) == 7
