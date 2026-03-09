"""Tests for test module 616 — covers src modules [2461, 2462, 2463, 2464]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2461 import modulo_2461
from module_2462 import power_2462
from module_2463 import min_2463
from module_2464 import max_2464

def test_modulo_2461():
    assert modulo_2461(10, 3) == 1

def test_power_2462():
    assert power_2462(2, 8) == 256

def test_min_2463():
    assert min_2463(3, 7) == 3

def test_max_2464():
    assert max_2464(3, 7) == 7
