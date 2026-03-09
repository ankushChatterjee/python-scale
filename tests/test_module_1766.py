"""Tests for test module 1766 — covers src modules [7061, 7062, 7063, 7064]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7061 import modulo_7061
from module_7062 import power_7062
from module_7063 import min_7063
from module_7064 import max_7064

def test_modulo_7061():
    assert modulo_7061(10, 3) == 1

def test_power_7062():
    assert power_7062(2, 8) == 256

def test_min_7063():
    assert min_7063(3, 7) == 3

def test_max_7064():
    assert max_7064(3, 7) == 7
