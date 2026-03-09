"""Tests for test module 1266 — covers src modules [5061, 5062, 5063, 5064]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5061 import modulo_5061
from module_5062 import power_5062
from module_5063 import min_5063
from module_5064 import max_5064

def test_modulo_5061():
    assert modulo_5061(10, 3) == 1

def test_power_5062():
    assert power_5062(2, 8) == 256

def test_min_5063():
    assert min_5063(3, 7) == 3

def test_max_5064():
    assert max_5064(3, 7) == 7
