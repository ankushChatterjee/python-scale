"""Tests for test module 1590 — covers src modules [6357, 6358, 6359, 6360]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6357 import modulo_6357
from module_6358 import power_6358
from module_6359 import min_6359
from module_6360 import max_6360

def test_modulo_6357():
    assert modulo_6357(10, 3) == 1

def test_power_6358():
    assert power_6358(2, 8) == 256

def test_min_6359():
    assert min_6359(3, 7) == 3

def test_max_6360():
    assert max_6360(3, 7) == 7
