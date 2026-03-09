"""Tests for test module 2108 — covers src modules [8429, 8430, 8431, 8432]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8429 import modulo_8429
from module_8430 import power_8430
from module_8431 import min_8431
from module_8432 import max_8432

def test_modulo_8429():
    assert modulo_8429(10, 3) == 1

def test_power_8430():
    assert power_8430(2, 8) == 256

def test_min_8431():
    assert min_8431(3, 7) == 3

def test_max_8432():
    assert max_8432(3, 7) == 7
