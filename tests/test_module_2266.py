"""Tests for test module 2266 — covers src modules [9061, 9062, 9063, 9064]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9061 import modulo_9061
from module_9062 import power_9062
from module_9063 import min_9063
from module_9064 import max_9064

def test_modulo_9061():
    assert modulo_9061(10, 3) == 1

def test_power_9062():
    assert power_9062(2, 8) == 256

def test_min_9063():
    assert min_9063(3, 7) == 3

def test_max_9064():
    assert max_9064(3, 7) == 7
