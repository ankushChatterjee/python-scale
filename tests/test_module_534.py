"""Tests for test module 534 — covers src modules [2133, 2134, 2135, 2136]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2133 import modulo_2133
from module_2134 import power_2134
from module_2135 import min_2135
from module_2136 import max_2136

def test_modulo_2133():
    assert modulo_2133(10, 3) == 1

def test_power_2134():
    assert power_2134(2, 8) == 256

def test_min_2135():
    assert min_2135(3, 7) == 3

def test_max_2136():
    assert max_2136(3, 7) == 7
