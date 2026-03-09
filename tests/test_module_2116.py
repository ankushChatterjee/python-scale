"""Tests for test module 2116 — covers src modules [8461, 8462, 8463, 8464]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8461 import modulo_8461
from module_8462 import power_8462
from module_8463 import min_8463
from module_8464 import max_8464

def test_modulo_8461():
    assert modulo_8461(10, 3) == 1

def test_power_8462():
    assert power_8462(2, 8) == 256

def test_min_8463():
    assert min_8463(3, 7) == 3

def test_max_8464():
    assert max_8464(3, 7) == 7
