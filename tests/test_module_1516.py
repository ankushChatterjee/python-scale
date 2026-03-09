"""Tests for test module 1516 — covers src modules [6061, 6062, 6063, 6064]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6061 import modulo_6061
from module_6062 import power_6062
from module_6063 import min_6063
from module_6064 import max_6064

def test_modulo_6061():
    assert modulo_6061(10, 3) == 1

def test_power_6062():
    assert power_6062(2, 8) == 256

def test_min_6063():
    assert min_6063(3, 7) == 3

def test_max_6064():
    assert max_6064(3, 7) == 7
