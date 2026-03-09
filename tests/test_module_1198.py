"""Tests for test module 1198 — covers src modules [4789, 4790, 4791, 4792]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4789 import modulo_4789
from module_4790 import power_4790
from module_4791 import min_4791
from module_4792 import max_4792

def test_modulo_4789():
    assert modulo_4789(10, 3) == 1

def test_power_4790():
    assert power_4790(2, 8) == 256

def test_min_4791():
    assert min_4791(3, 7) == 3

def test_max_4792():
    assert max_4792(3, 7) == 7
