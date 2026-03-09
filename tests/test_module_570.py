"""Tests for test module 570 — covers src modules [2277, 2278, 2279, 2280]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2277 import modulo_2277
from module_2278 import power_2278
from module_2279 import min_2279
from module_2280 import max_2280

def test_modulo_2277():
    assert modulo_2277(10, 3) == 1

def test_power_2278():
    assert power_2278(2, 8) == 256

def test_min_2279():
    assert min_2279(3, 7) == 3

def test_max_2280():
    assert max_2280(3, 7) == 7
