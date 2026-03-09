"""Tests for test module 590 — covers src modules [2357, 2358, 2359, 2360]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2357 import modulo_2357
from module_2358 import power_2358
from module_2359 import min_2359
from module_2360 import max_2360

def test_modulo_2357():
    assert modulo_2357(10, 3) == 1

def test_power_2358():
    assert power_2358(2, 8) == 256

def test_min_2359():
    assert min_2359(3, 7) == 3

def test_max_2360():
    assert max_2360(3, 7) == 7
