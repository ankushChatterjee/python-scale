"""Tests for test module 1448 — covers src modules [5789, 5790, 5791, 5792]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5789 import modulo_5789
from module_5790 import power_5790
from module_5791 import min_5791
from module_5792 import max_5792

def test_modulo_5789():
    assert modulo_5789(10, 3) == 1

def test_power_5790():
    assert power_5790(2, 8) == 256

def test_min_5791():
    assert min_5791(3, 7) == 3

def test_max_5792():
    assert max_5792(3, 7) == 7
