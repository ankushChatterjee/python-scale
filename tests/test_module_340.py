"""Tests for test module 340 — covers src modules [1357, 1358, 1359, 1360]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1357 import modulo_1357
from module_1358 import power_1358
from module_1359 import min_1359
from module_1360 import max_1360

def test_modulo_1357():
    assert modulo_1357(10, 3) == 1

def test_power_1358():
    assert power_1358(2, 8) == 256

def test_min_1359():
    assert min_1359(3, 7) == 3

def test_max_1360():
    assert max_1360(3, 7) == 7
