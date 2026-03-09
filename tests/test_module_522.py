"""Tests for test module 522 — covers src modules [2085, 2086, 2087, 2088]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2085 import modulo_2085
from module_2086 import power_2086
from module_2087 import min_2087
from module_2088 import max_2088

def test_modulo_2085():
    assert modulo_2085(10, 3) == 1

def test_power_2086():
    assert power_2086(2, 8) == 256

def test_min_2087():
    assert min_2087(3, 7) == 3

def test_max_2088():
    assert max_2088(3, 7) == 7
