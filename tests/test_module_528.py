"""Tests for test module 528 — covers src modules [2109, 2110, 2111, 2112]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2109 import modulo_2109
from module_2110 import power_2110
from module_2111 import min_2111
from module_2112 import max_2112

def test_modulo_2109():
    assert modulo_2109(10, 3) == 1

def test_power_2110():
    assert power_2110(2, 8) == 256

def test_min_2111():
    assert min_2111(3, 7) == 3

def test_max_2112():
    assert max_2112(3, 7) == 7
