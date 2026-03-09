"""Tests for test module 2198 — covers src modules [8789, 8790, 8791, 8792]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8789 import modulo_8789
from module_8790 import power_8790
from module_8791 import min_8791
from module_8792 import max_8792

def test_modulo_8789():
    assert modulo_8789(10, 3) == 1

def test_power_8790():
    assert power_8790(2, 8) == 256

def test_min_8791():
    assert min_8791(3, 7) == 3

def test_max_8792():
    assert max_8792(3, 7) == 7
