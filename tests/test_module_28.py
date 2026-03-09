"""Tests for test module 28 — covers src modules [109, 110, 111, 112]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_109 import modulo_109
from module_110 import power_110
from module_111 import min_111
from module_112 import max_112

def test_modulo_109():
    assert modulo_109(10, 3) == 1

def test_power_110():
    assert power_110(2, 8) == 256

def test_min_111():
    assert min_111(3, 7) == 3

def test_max_112():
    assert max_112(3, 7) == 7
