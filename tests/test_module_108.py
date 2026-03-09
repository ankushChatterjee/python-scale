"""Tests for test module 108 — covers src modules [429, 430, 431, 432]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_429 import modulo_429
from module_430 import power_430
from module_431 import min_431
from module_432 import max_432

def test_modulo_429():
    assert modulo_429(10, 3) == 1

def test_power_430():
    assert power_430(2, 8) == 256

def test_min_431():
    assert min_431(3, 7) == 3

def test_max_432():
    assert max_432(3, 7) == 7
