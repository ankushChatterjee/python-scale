"""Tests for test module 1698 — covers src modules [6789, 6790, 6791, 6792]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6789 import modulo_6789
from module_6790 import power_6790
from module_6791 import min_6791
from module_6792 import max_6792

def test_modulo_6789():
    assert modulo_6789(10, 3) == 1

def test_power_6790():
    assert power_6790(2, 8) == 256

def test_min_6791():
    assert min_6791(3, 7) == 3

def test_max_6792():
    assert max_6792(3, 7) == 7
