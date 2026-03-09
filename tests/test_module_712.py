"""Tests for test module 712 — covers src modules [2845, 2846, 2847, 2848]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2845 import modulo_2845
from module_2846 import power_2846
from module_2847 import min_2847
from module_2848 import max_2848

def test_modulo_2845():
    assert modulo_2845(10, 3) == 1

def test_power_2846():
    assert power_2846(2, 8) == 256

def test_min_2847():
    assert min_2847(3, 7) == 3

def test_max_2848():
    assert max_2848(3, 7) == 7
