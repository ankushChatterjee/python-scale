"""Tests for test module 1274 — covers src modules [5093, 5094, 5095, 5096]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5093 import modulo_5093
from module_5094 import power_5094
from module_5095 import min_5095
from module_5096 import max_5096

def test_modulo_5093():
    assert modulo_5093(10, 3) == 1

def test_power_5094():
    assert power_5094(2, 8) == 256

def test_min_5095():
    assert min_5095(3, 7) == 3

def test_max_5096():
    assert max_5096(3, 7) == 7
