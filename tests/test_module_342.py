"""Tests for test module 342 — covers src modules [1365, 1366, 1367, 1368]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1365 import modulo_1365
from module_1366 import power_1366
from module_1367 import min_1367
from module_1368 import max_1368

def test_modulo_1365():
    assert modulo_1365(10, 3) == 1

def test_power_1366():
    assert power_1366(2, 8) == 256

def test_min_1367():
    assert min_1367(3, 7) == 3

def test_max_1368():
    assert max_1368(3, 7) == 7
