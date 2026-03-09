"""Tests for test module 2028 — covers src modules [8109, 8110, 8111, 8112]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8109 import modulo_8109
from module_8110 import power_8110
from module_8111 import min_8111
from module_8112 import max_8112

def test_modulo_8109():
    assert modulo_8109(10, 3) == 1

def test_power_8110():
    assert power_8110(2, 8) == 256

def test_min_8111():
    assert min_8111(3, 7) == 3

def test_max_8112():
    assert max_8112(3, 7) == 7
