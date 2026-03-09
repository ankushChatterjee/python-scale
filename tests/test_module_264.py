"""Tests for test module 264 — covers src modules [1053, 1054, 1055, 1056]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1053 import modulo_1053
from module_1054 import power_1054
from module_1055 import min_1055
from module_1056 import max_1056

def test_modulo_1053():
    assert modulo_1053(10, 3) == 1

def test_power_1054():
    assert power_1054(2, 8) == 256

def test_min_1055():
    assert min_1055(3, 7) == 3

def test_max_1056():
    assert max_1056(3, 7) == 7
