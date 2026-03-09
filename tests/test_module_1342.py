"""Tests for test module 1342 — covers src modules [5365, 5366, 5367, 5368]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5365 import modulo_5365
from module_5366 import power_5366
from module_5367 import min_5367
from module_5368 import max_5368

def test_modulo_5365():
    assert modulo_5365(10, 3) == 1

def test_power_5366():
    assert power_5366(2, 8) == 256

def test_min_5367():
    assert min_5367(3, 7) == 3

def test_max_5368():
    assert max_5368(3, 7) == 7
