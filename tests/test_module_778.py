"""Tests for test module 778 — covers src modules [3109, 3110, 3111, 3112]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3109 import modulo_3109
from module_3110 import power_3110
from module_3111 import min_3111
from module_3112 import max_3112

def test_modulo_3109():
    assert modulo_3109(10, 3) == 1

def test_power_3110():
    assert power_3110(2, 8) == 256

def test_min_3111():
    assert min_3111(3, 7) == 3

def test_max_3112():
    assert max_3112(3, 7) == 7
