"""Tests for test module 1016 — covers src modules [4061, 4062, 4063, 4064]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4061 import modulo_4061
from module_4062 import power_4062
from module_4063 import min_4063
from module_4064 import max_4064

def test_modulo_4061():
    assert modulo_4061(10, 3) == 1

def test_power_4062():
    assert power_4062(2, 8) == 256

def test_min_4063():
    assert min_4063(3, 7) == 3

def test_max_4064():
    assert max_4064(3, 7) == 7
