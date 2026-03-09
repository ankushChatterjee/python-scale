"""Tests for test module 1278 — covers src modules [5109, 5110, 5111, 5112]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5109 import modulo_5109
from module_5110 import power_5110
from module_5111 import min_5111
from module_5112 import max_5112

def test_modulo_5109():
    assert modulo_5109(10, 3) == 1

def test_power_5110():
    assert power_5110(2, 8) == 256

def test_min_5111():
    assert min_5111(3, 7) == 3

def test_max_5112():
    assert max_5112(3, 7) == 7
