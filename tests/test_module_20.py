"""Tests for test module 20 — covers src modules [77, 78, 79, 80]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_77 import modulo_77
from module_78 import power_78
from module_79 import min_79
from module_80 import max_80

def test_modulo_77():
    assert modulo_77(10, 3) == 1

def test_power_78():
    assert power_78(2, 8) == 256

def test_min_79():
    assert min_79(3, 7) == 3

def test_max_80():
    assert max_80(3, 7) == 7
