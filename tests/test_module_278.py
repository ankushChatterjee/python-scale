"""Tests for test module 278 — covers src modules [1109, 1110, 1111, 1112]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1109 import modulo_1109
from module_1110 import power_1110
from module_1111 import min_1111
from module_1112 import max_1112

def test_modulo_1109():
    assert modulo_1109(10, 3) == 1

def test_power_1110():
    assert power_1110(2, 8) == 256

def test_min_1111():
    assert min_1111(3, 7) == 3

def test_max_1112():
    assert max_1112(3, 7) == 7
