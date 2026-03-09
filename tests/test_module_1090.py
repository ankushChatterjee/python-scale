"""Tests for test module 1090 — covers src modules [4357, 4358, 4359, 4360]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4357 import modulo_4357
from module_4358 import power_4358
from module_4359 import min_4359
from module_4360 import max_4360

def test_modulo_4357():
    assert modulo_4357(10, 3) == 1

def test_power_4358():
    assert power_4358(2, 8) == 256

def test_min_4359():
    assert min_4359(3, 7) == 3

def test_max_4360():
    assert max_4360(3, 7) == 7
