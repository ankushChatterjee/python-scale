"""Tests for test module 34 — covers src modules [133, 134, 135, 136]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_133 import modulo_133
from module_134 import power_134
from module_135 import min_135
from module_136 import max_136

def test_modulo_133():
    assert modulo_133(10, 3) == 1

def test_power_134():
    assert power_134(2, 8) == 256

def test_min_135():
    assert min_135(3, 7) == 3

def test_max_136():
    assert max_136(3, 7) == 7
