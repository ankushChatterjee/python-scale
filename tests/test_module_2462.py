"""Tests for test module 2462 — covers src modules [9845, 9846, 9847, 9848]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9845 import modulo_9845
from module_9846 import power_9846
from module_9847 import min_9847
from module_9848 import max_9848

def test_modulo_9845():
    assert modulo_9845(10, 3) == 1

def test_power_9846():
    assert power_9846(2, 8) == 256

def test_min_9847():
    assert min_9847(3, 7) == 3

def test_max_9848():
    assert max_9848(3, 7) == 7
