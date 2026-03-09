"""Tests for test module 1366 — covers src modules [5461, 5462, 5463, 5464]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5461 import modulo_5461
from module_5462 import power_5462
from module_5463 import min_5463
from module_5464 import max_5464

def test_modulo_5461():
    assert modulo_5461(10, 3) == 1

def test_power_5462():
    assert power_5462(2, 8) == 256

def test_min_5463():
    assert min_5463(3, 7) == 3

def test_max_5464():
    assert max_5464(3, 7) == 7
