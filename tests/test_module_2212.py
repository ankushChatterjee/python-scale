"""Tests for test module 2212 — covers src modules [8845, 8846, 8847, 8848]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8845 import modulo_8845
from module_8846 import power_8846
from module_8847 import min_8847
from module_8848 import max_8848

def test_modulo_8845():
    assert modulo_8845(10, 3) == 1

def test_power_8846():
    assert power_8846(2, 8) == 256

def test_min_8847():
    assert min_8847(3, 7) == 3

def test_max_8848():
    assert max_8848(3, 7) == 7
