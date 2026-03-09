"""Tests for test module 1328 — covers src modules [5309, 5310, 5311, 5312]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5309 import modulo_5309
from module_5310 import power_5310
from module_5311 import min_5311
from module_5312 import max_5312

def test_modulo_5309():
    assert modulo_5309(10, 3) == 1

def test_power_5310():
    assert power_5310(2, 8) == 256

def test_min_5311():
    assert min_5311(3, 7) == 3

def test_max_5312():
    assert max_5312(3, 7) == 7
