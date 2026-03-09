"""Tests for test module 1784 — covers src modules [7133, 7134, 7135, 7136]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7133 import modulo_7133
from module_7134 import power_7134
from module_7135 import min_7135
from module_7136 import max_7136

def test_modulo_7133():
    assert modulo_7133(10, 3) == 1

def test_power_7134():
    assert power_7134(2, 8) == 256

def test_min_7135():
    assert min_7135(3, 7) == 3

def test_max_7136():
    assert max_7136(3, 7) == 7
