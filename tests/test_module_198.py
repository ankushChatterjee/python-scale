"""Tests for test module 198 — covers src modules [789, 790, 791, 792]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_789 import modulo_789
from module_790 import power_790
from module_791 import min_791
from module_792 import max_792

def test_modulo_789():
    assert modulo_789(10, 3) == 1

def test_power_790():
    assert power_790(2, 8) == 256

def test_min_791():
    assert min_791(3, 7) == 3

def test_max_792():
    assert max_792(3, 7) == 7
