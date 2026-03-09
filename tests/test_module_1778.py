"""Tests for test module 1778 — covers src modules [7109, 7110, 7111, 7112]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7109 import modulo_7109
from module_7110 import power_7110
from module_7111 import min_7111
from module_7112 import max_7112

def test_modulo_7109():
    assert modulo_7109(10, 3) == 1

def test_power_7110():
    assert power_7110(2, 8) == 256

def test_min_7111():
    assert min_7111(3, 7) == 3

def test_max_7112():
    assert max_7112(3, 7) == 7
