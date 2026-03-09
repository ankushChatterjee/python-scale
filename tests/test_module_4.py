"""Tests for test module 4 — covers src modules [13, 14, 15, 16]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_13 import modulo_13
from module_14 import power_14
from module_15 import min_15
from module_16 import max_16

def test_modulo_13():
    assert modulo_13(10, 3) == 1

def test_power_14():
    assert power_14(2, 8) == 256

def test_min_15():
    assert min_15(3, 7) == 3

def test_max_16():
    assert max_16(3, 7) == 7
