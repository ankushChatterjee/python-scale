"""Tests for test module 78 — covers src modules [309, 310, 311, 312]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_309 import modulo_309
from module_310 import power_310
from module_311 import min_311
from module_312 import max_312

def test_modulo_309():
    assert modulo_309(10, 3) == 1

def test_power_310():
    assert power_310(2, 8) == 256

def test_min_311():
    assert min_311(3, 7) == 3

def test_max_312():
    assert max_312(3, 7) == 7
