"""Tests for test module 2 — covers src modules [5, 6, 7, 8]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5 import modulo_5
from module_6 import power_6
from module_7 import min_7
from module_8 import max_8

def test_modulo_5():
    assert modulo_5(10, 3) == 1

def test_power_6():
    assert power_6(2, 8) == 256

def test_min_7():
    assert min_7(3, 7) == 3

def test_max_8():
    assert max_8(3, 7) == 7
