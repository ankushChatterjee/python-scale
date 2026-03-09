"""Tests for test module 1034 — covers src modules [4133, 4134, 4135, 4136]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4133 import modulo_4133
from module_4134 import power_4134
from module_4135 import min_4135
from module_4136 import max_4136

def test_modulo_4133():
    assert modulo_4133(10, 3) == 1

def test_power_4134():
    assert power_4134(2, 8) == 256

def test_min_4135():
    assert min_4135(3, 7) == 3

def test_max_4136():
    assert max_4136(3, 7) == 7
