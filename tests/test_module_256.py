"""Tests for test module 256 — covers src modules [1021, 1022, 1023, 1024]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1021 import modulo_1021
from module_1022 import power_1022
from module_1023 import min_1023
from module_1024 import max_1024

def test_modulo_1021():
    assert modulo_1021(10, 3) == 1

def test_power_1022():
    assert power_1022(2, 8) == 256

def test_min_1023():
    assert min_1023(3, 7) == 3

def test_max_1024():
    assert max_1024(3, 7) == 7
