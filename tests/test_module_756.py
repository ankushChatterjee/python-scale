"""Tests for test module 756 — covers src modules [3021, 3022, 3023, 3024]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3021 import modulo_3021
from module_3022 import power_3022
from module_3023 import min_3023
from module_3024 import max_3024

def test_modulo_3021():
    assert modulo_3021(10, 3) == 1

def test_power_3022():
    assert power_3022(2, 8) == 256

def test_min_3023():
    assert min_3023(3, 7) == 3

def test_max_3024():
    assert max_3024(3, 7) == 7
