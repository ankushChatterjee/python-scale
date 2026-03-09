"""Tests for test module 266 — covers src modules [1061, 1062, 1063, 1064]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1061 import modulo_1061
from module_1062 import power_1062
from module_1063 import min_1063
from module_1064 import max_1064

def test_modulo_1061():
    assert modulo_1061(10, 3) == 1

def test_power_1062():
    assert power_1062(2, 8) == 256

def test_min_1063():
    assert min_1063(3, 7) == 3

def test_max_1064():
    assert max_1064(3, 7) == 7
