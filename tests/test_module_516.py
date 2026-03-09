"""Tests for test module 516 — covers src modules [2061, 2062, 2063, 2064]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2061 import modulo_2061
from module_2062 import power_2062
from module_2063 import min_2063
from module_2064 import max_2064

def test_modulo_2061():
    assert modulo_2061(10, 3) == 1

def test_power_2062():
    assert power_2062(2, 8) == 256

def test_min_2063():
    assert min_2063(3, 7) == 3

def test_max_2064():
    assert max_2064(3, 7) == 7
