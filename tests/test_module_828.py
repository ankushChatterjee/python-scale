"""Tests for test module 828 — covers src modules [3309, 3310, 3311, 3312]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3309 import modulo_3309
from module_3310 import power_3310
from module_3311 import min_3311
from module_3312 import max_3312

def test_modulo_3309():
    assert modulo_3309(10, 3) == 1

def test_power_3310():
    assert power_3310(2, 8) == 256

def test_min_3311():
    assert min_3311(3, 7) == 3

def test_max_3312():
    assert max_3312(3, 7) == 7
