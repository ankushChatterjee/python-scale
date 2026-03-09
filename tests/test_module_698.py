"""Tests for test module 698 — covers src modules [2789, 2790, 2791, 2792]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2789 import modulo_2789
from module_2790 import power_2790
from module_2791 import min_2791
from module_2792 import max_2792

def test_modulo_2789():
    assert modulo_2789(10, 3) == 1

def test_power_2790():
    assert power_2790(2, 8) == 256

def test_min_2791():
    assert min_2791(3, 7) == 3

def test_max_2792():
    assert max_2792(3, 7) == 7
