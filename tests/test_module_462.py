"""Tests for test module 462 — covers src modules [1845, 1846, 1847, 1848]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1845 import modulo_1845
from module_1846 import power_1846
from module_1847 import min_1847
from module_1848 import max_1848

def test_modulo_1845():
    assert modulo_1845(10, 3) == 1

def test_power_1846():
    assert power_1846(2, 8) == 256

def test_min_1847():
    assert min_1847(3, 7) == 3

def test_max_1848():
    assert max_1848(3, 7) == 7
