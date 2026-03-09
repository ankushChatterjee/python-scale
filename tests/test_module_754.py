"""Tests for test module 754 — covers src modules [3013, 3014, 3015, 3016]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3013 import modulo_3013
from module_3014 import power_3014
from module_3015 import min_3015
from module_3016 import max_3016

def test_modulo_3013():
    assert modulo_3013(10, 3) == 1

def test_power_3014():
    assert power_3014(2, 8) == 256

def test_min_3015():
    assert min_3015(3, 7) == 3

def test_max_3016():
    assert max_3016(3, 7) == 7
