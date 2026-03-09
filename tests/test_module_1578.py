"""Tests for test module 1578 — covers src modules [6309, 6310, 6311, 6312]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6309 import modulo_6309
from module_6310 import power_6310
from module_6311 import min_6311
from module_6312 import max_6312

def test_modulo_6309():
    assert modulo_6309(10, 3) == 1

def test_power_6310():
    assert power_6310(2, 8) == 256

def test_min_6311():
    assert min_6311(3, 7) == 3

def test_max_6312():
    assert max_6312(3, 7) == 7
