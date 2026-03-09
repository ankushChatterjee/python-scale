"""Tests for test module 1256 — covers src modules [5021, 5022, 5023, 5024]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5021 import modulo_5021
from module_5022 import power_5022
from module_5023 import min_5023
from module_5024 import max_5024

def test_modulo_5021():
    assert modulo_5021(10, 3) == 1

def test_power_5022():
    assert power_5022(2, 8) == 256

def test_min_5023():
    assert min_5023(3, 7) == 3

def test_max_5024():
    assert max_5024(3, 7) == 7
