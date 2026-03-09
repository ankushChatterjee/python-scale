"""Tests for test module 254 — covers src modules [1013, 1014, 1015, 1016]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1013 import modulo_1013
from module_1014 import power_1014
from module_1015 import min_1015
from module_1016 import max_1016

def test_modulo_1013():
    assert modulo_1013(10, 3) == 1

def test_power_1014():
    assert power_1014(2, 8) == 256

def test_min_1015():
    assert min_1015(3, 7) == 3

def test_max_1016():
    assert max_1016(3, 7) == 7
