"""Tests for test module 1790 — covers src modules [7157, 7158, 7159, 7160]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7157 import modulo_7157
from module_7158 import power_7158
from module_7159 import min_7159
from module_7160 import max_7160

def test_modulo_7157():
    assert modulo_7157(10, 3) == 1

def test_power_7158():
    assert power_7158(2, 8) == 256

def test_min_7159():
    assert min_7159(3, 7) == 3

def test_max_7160():
    assert max_7160(3, 7) == 7
