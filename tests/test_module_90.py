"""Tests for test module 90 — covers src modules [357, 358, 359, 360]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_357 import modulo_357
from module_358 import power_358
from module_359 import min_359
from module_360 import max_360

def test_modulo_357():
    assert modulo_357(10, 3) == 1

def test_power_358():
    assert power_358(2, 8) == 256

def test_min_359():
    assert min_359(3, 7) == 3

def test_max_360():
    assert max_360(3, 7) == 7
