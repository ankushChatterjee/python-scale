"""Tests for test module 448 — covers src modules [1789, 1790, 1791, 1792]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1789 import modulo_1789
from module_1790 import power_1790
from module_1791 import min_1791
from module_1792 import max_1792

def test_modulo_1789():
    assert modulo_1789(10, 3) == 1

def test_power_1790():
    assert power_1790(2, 8) == 256

def test_min_1791():
    assert min_1791(3, 7) == 3

def test_max_1792():
    assert max_1792(3, 7) == 7
