"""Tests for test module 1948 — covers src modules [7789, 7790, 7791, 7792]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7789 import modulo_7789
from module_7790 import power_7790
from module_7791 import min_7791
from module_7792 import max_7792

def test_modulo_7789():
    assert modulo_7789(10, 3) == 1

def test_power_7790():
    assert power_7790(2, 8) == 256

def test_min_7791():
    assert min_7791(3, 7) == 3

def test_max_7792():
    assert max_7792(3, 7) == 7
