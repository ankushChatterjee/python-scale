"""Tests for test module 358 — covers src modules [1429, 1430, 1431, 1432]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1429 import modulo_1429
from module_1430 import power_1430
from module_1431 import min_1431
from module_1432 import max_1432

def test_modulo_1429():
    assert modulo_1429(10, 3) == 1

def test_power_1430():
    assert power_1430(2, 8) == 256

def test_min_1431():
    assert min_1431(3, 7) == 3

def test_max_1432():
    assert max_1432(3, 7) == 7
