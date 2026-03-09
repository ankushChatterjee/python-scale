"""Tests for test module 514 — covers src modules [2053, 2054, 2055, 2056]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2053 import modulo_2053
from module_2054 import power_2054
from module_2055 import min_2055
from module_2056 import max_2056

def test_modulo_2053():
    assert modulo_2053(10, 3) == 1

def test_power_2054():
    assert power_2054(2, 8) == 256

def test_min_2055():
    assert min_2055(3, 7) == 3

def test_max_2056():
    assert max_2056(3, 7) == 7
