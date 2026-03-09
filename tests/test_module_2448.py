"""Tests for test module 2448 — covers src modules [9789, 9790, 9791, 9792]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9789 import modulo_9789
from module_9790 import power_9790
from module_9791 import min_9791
from module_9792 import max_9792

def test_modulo_9789():
    assert modulo_9789(10, 3) == 1

def test_power_9790():
    assert power_9790(2, 8) == 256

def test_min_9791():
    assert min_9791(3, 7) == 3

def test_max_9792():
    assert max_9792(3, 7) == 7
