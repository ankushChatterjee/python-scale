"""Tests for test module 1828 — covers src modules [7309, 7310, 7311, 7312]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7309 import modulo_7309
from module_7310 import power_7310
from module_7311 import min_7311
from module_7312 import max_7312

def test_modulo_7309():
    assert modulo_7309(10, 3) == 1

def test_power_7310():
    assert power_7310(2, 8) == 256

def test_min_7311():
    assert min_7311(3, 7) == 3

def test_max_7312():
    assert max_7312(3, 7) == 7
