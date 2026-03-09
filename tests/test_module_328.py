"""Tests for test module 328 — covers src modules [1309, 1310, 1311, 1312]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1309 import modulo_1309
from module_1310 import power_1310
from module_1311 import min_1311
from module_1312 import max_1312

def test_modulo_1309():
    assert modulo_1309(10, 3) == 1

def test_power_1310():
    assert power_1310(2, 8) == 256

def test_min_1311():
    assert min_1311(3, 7) == 3

def test_max_1312():
    assert max_1312(3, 7) == 7
