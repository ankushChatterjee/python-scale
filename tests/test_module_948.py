"""Tests for test module 948 — covers src modules [3789, 3790, 3791, 3792]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3789 import modulo_3789
from module_3790 import power_3790
from module_3791 import min_3791
from module_3792 import max_3792

def test_modulo_3789():
    assert modulo_3789(10, 3) == 1

def test_power_3790():
    assert power_3790(2, 8) == 256

def test_min_3791():
    assert min_3791(3, 7) == 3

def test_max_3792():
    assert max_3792(3, 7) == 7
