"""Tests for test module 2328 — covers src modules [9309, 9310, 9311, 9312]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9309 import modulo_9309
from module_9310 import power_9310
from module_9311 import min_9311
from module_9312 import max_9312

def test_modulo_9309():
    assert modulo_9309(10, 3) == 1

def test_power_9310():
    assert power_9310(2, 8) == 256

def test_min_9311():
    assert min_9311(3, 7) == 3

def test_max_9312():
    assert max_9312(3, 7) == 7
