"""Tests for test module 1962 — covers src modules [7845, 7846, 7847, 7848]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7845 import modulo_7845
from module_7846 import power_7846
from module_7847 import min_7847
from module_7848 import max_7848

def test_modulo_7845():
    assert modulo_7845(10, 3) == 1

def test_power_7846():
    assert power_7846(2, 8) == 256

def test_min_7847():
    assert min_7847(3, 7) == 3

def test_max_7848():
    assert max_7848(3, 7) == 7
