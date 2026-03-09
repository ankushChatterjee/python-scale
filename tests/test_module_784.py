"""Tests for test module 784 — covers src modules [3133, 3134, 3135, 3136]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3133 import modulo_3133
from module_3134 import power_3134
from module_3135 import min_3135
from module_3136 import max_3136

def test_modulo_3133():
    assert modulo_3133(10, 3) == 1

def test_power_3134():
    assert power_3134(2, 8) == 256

def test_min_3135():
    assert min_3135(3, 7) == 3

def test_max_3136():
    assert max_3136(3, 7) == 7
