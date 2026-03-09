"""Tests for test module 1964 — covers src modules [7853, 7854, 7855, 7856]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7853 import modulo_7853
from module_7854 import power_7854
from module_7855 import min_7855
from module_7856 import max_7856

def test_modulo_7853():
    assert modulo_7853(10, 3) == 1

def test_power_7854():
    assert power_7854(2, 8) == 256

def test_min_7855():
    assert min_7855(3, 7) == 3

def test_max_7856():
    assert max_7856(3, 7) == 7
