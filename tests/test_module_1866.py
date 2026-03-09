"""Tests for test module 1866 — covers src modules [7461, 7462, 7463, 7464]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7461 import modulo_7461
from module_7462 import power_7462
from module_7463 import min_7463
from module_7464 import max_7464

def test_modulo_7461():
    assert modulo_7461(10, 3) == 1

def test_power_7462():
    assert power_7462(2, 8) == 256

def test_min_7463():
    assert min_7463(3, 7) == 3

def test_max_7464():
    assert max_7464(3, 7) == 7
