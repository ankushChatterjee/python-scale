"""Tests for test module 1528 — covers src modules [6109, 6110, 6111, 6112]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6109 import modulo_6109
from module_6110 import power_6110
from module_6111 import min_6111
from module_6112 import max_6112

def test_modulo_6109():
    assert modulo_6109(10, 3) == 1

def test_power_6110():
    assert power_6110(2, 8) == 256

def test_min_6111():
    assert min_6111(3, 7) == 3

def test_max_6112():
    assert max_6112(3, 7) == 7
