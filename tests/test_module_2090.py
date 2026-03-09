"""Tests for test module 2090 — covers src modules [8357, 8358, 8359, 8360]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8357 import modulo_8357
from module_8358 import power_8358
from module_8359 import min_8359
from module_8360 import max_8360

def test_modulo_8357():
    assert modulo_8357(10, 3) == 1

def test_power_8358():
    assert power_8358(2, 8) == 256

def test_min_8359():
    assert min_8359(3, 7) == 3

def test_max_8360():
    assert max_8360(3, 7) == 7
