"""Tests for test module 274 — covers src modules [1093, 1094, 1095, 1096]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1093 import modulo_1093
from module_1094 import power_1094
from module_1095 import min_1095
from module_1096 import max_1096

def test_modulo_1093():
    assert modulo_1093(10, 3) == 1

def test_power_1094():
    assert power_1094(2, 8) == 256

def test_min_1095():
    assert min_1095(3, 7) == 3

def test_max_1096():
    assert max_1096(3, 7) == 7
