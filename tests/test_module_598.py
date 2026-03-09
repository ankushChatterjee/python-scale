"""Tests for test module 598 — covers src modules [2389, 2390, 2391, 2392]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2389 import modulo_2389
from module_2390 import power_2390
from module_2391 import min_2391
from module_2392 import max_2392

def test_modulo_2389():
    assert modulo_2389(10, 3) == 1

def test_power_2390():
    assert power_2390(2, 8) == 256

def test_min_2391():
    assert min_2391(3, 7) == 3

def test_max_2392():
    assert max_2392(3, 7) == 7
