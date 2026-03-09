"""Tests for test module 2094 — covers src modules [8373, 8374, 8375, 8376]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8373 import modulo_8373
from module_8374 import power_8374
from module_8375 import min_8375
from module_8376 import max_8376

def test_modulo_8373():
    assert modulo_8373(10, 3) == 1

def test_power_8374():
    assert power_8374(2, 8) == 256

def test_min_8375():
    assert min_8375(3, 7) == 3

def test_max_8376():
    assert max_8376(3, 7) == 7
