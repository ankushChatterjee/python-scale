"""Tests for test module 284 — covers src modules [1133, 1134, 1135, 1136]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1133 import modulo_1133
from module_1134 import power_1134
from module_1135 import min_1135
from module_1136 import max_1136

def test_modulo_1133():
    assert modulo_1133(10, 3) == 1

def test_power_1134():
    assert power_1134(2, 8) == 256

def test_min_1135():
    assert min_1135(3, 7) == 3

def test_max_1136():
    assert max_1136(3, 7) == 7
