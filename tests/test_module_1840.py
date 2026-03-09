"""Tests for test module 1840 — covers src modules [7357, 7358, 7359, 7360]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7357 import modulo_7357
from module_7358 import power_7358
from module_7359 import min_7359
from module_7360 import max_7360

def test_modulo_7357():
    assert modulo_7357(10, 3) == 1

def test_power_7358():
    assert power_7358(2, 8) == 256

def test_min_7359():
    assert min_7359(3, 7) == 3

def test_max_7360():
    assert max_7360(3, 7) == 7
