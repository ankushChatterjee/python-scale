"""Tests for test module 1836 — covers src modules [7341, 7342, 7343, 7344]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7341 import modulo_7341
from module_7342 import power_7342
from module_7343 import min_7343
from module_7344 import max_7344

def test_modulo_7341():
    assert modulo_7341(10, 3) == 1

def test_power_7342():
    assert power_7342(2, 8) == 256

def test_min_7343():
    assert min_7343(3, 7) == 3

def test_max_7344():
    assert max_7344(3, 7) == 7
