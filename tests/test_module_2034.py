"""Tests for test module 2034 — covers src modules [8133, 8134, 8135, 8136]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8133 import modulo_8133
from module_8134 import power_8134
from module_8135 import min_8135
from module_8136 import max_8136

def test_modulo_8133():
    assert modulo_8133(10, 3) == 1

def test_power_8134():
    assert power_8134(2, 8) == 256

def test_min_8135():
    assert min_8135(3, 7) == 3

def test_max_8136():
    assert max_8136(3, 7) == 7
