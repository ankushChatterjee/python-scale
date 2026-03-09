"""Tests for test module 764 — covers src modules [3053, 3054, 3055, 3056]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3053 import modulo_3053
from module_3054 import power_3054
from module_3055 import min_3055
from module_3056 import max_3056

def test_modulo_3053():
    assert modulo_3053(10, 3) == 1

def test_power_3054():
    assert power_3054(2, 8) == 256

def test_min_3055():
    assert min_3055(3, 7) == 3

def test_max_3056():
    assert max_3056(3, 7) == 7
