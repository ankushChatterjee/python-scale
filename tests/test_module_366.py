"""Tests for test module 366 — covers src modules [1461, 1462, 1463, 1464]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1461 import modulo_1461
from module_1462 import power_1462
from module_1463 import min_1463
from module_1464 import max_1464

def test_modulo_1461():
    assert modulo_1461(10, 3) == 1

def test_power_1462():
    assert power_1462(2, 8) == 256

def test_min_1463():
    assert min_1463(3, 7) == 3

def test_max_1464():
    assert max_1464(3, 7) == 7
