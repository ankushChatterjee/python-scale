"""Tests for test module 1712 — covers src modules [6845, 6846, 6847, 6848]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6845 import modulo_6845
from module_6846 import power_6846
from module_6847 import min_6847
from module_6848 import max_6848

def test_modulo_6845():
    assert modulo_6845(10, 3) == 1

def test_power_6846():
    assert power_6846(2, 8) == 256

def test_min_6847():
    assert min_6847(3, 7) == 3

def test_max_6848():
    assert max_6848(3, 7) == 7
