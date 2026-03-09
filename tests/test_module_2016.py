"""Tests for test module 2016 — covers src modules [8061, 8062, 8063, 8064]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8061 import modulo_8061
from module_8062 import power_8062
from module_8063 import min_8063
from module_8064 import max_8064

def test_modulo_8061():
    assert modulo_8061(10, 3) == 1

def test_power_8062():
    assert power_8062(2, 8) == 256

def test_min_8063():
    assert min_8063(3, 7) == 3

def test_max_8064():
    assert max_8064(3, 7) == 7
