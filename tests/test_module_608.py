"""Tests for test module 608 — covers src modules [2429, 2430, 2431, 2432]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2429 import modulo_2429
from module_2430 import power_2430
from module_2431 import min_2431
from module_2432 import max_2432

def test_modulo_2429():
    assert modulo_2429(10, 3) == 1

def test_power_2430():
    assert power_2430(2, 8) == 256

def test_min_2431():
    assert min_2431(3, 7) == 3

def test_max_2432():
    assert max_2432(3, 7) == 7
