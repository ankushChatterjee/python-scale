"""Tests for test module 2078 — covers src modules [8309, 8310, 8311, 8312]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8309 import modulo_8309
from module_8310 import power_8310
from module_8311 import min_8311
from module_8312 import max_8312

def test_modulo_8309():
    assert modulo_8309(10, 3) == 1

def test_power_8310():
    assert power_8310(2, 8) == 256

def test_min_8311():
    assert min_8311(3, 7) == 3

def test_max_8312():
    assert max_8312(3, 7) == 7
