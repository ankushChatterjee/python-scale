"""Tests for test module 1506 — covers src modules [6021, 6022, 6023, 6024]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6021 import modulo_6021
from module_6022 import power_6022
from module_6023 import min_6023
from module_6024 import max_6024

def test_modulo_6021():
    assert modulo_6021(10, 3) == 1

def test_power_6022():
    assert power_6022(2, 8) == 256

def test_min_6023():
    assert min_6023(3, 7) == 3

def test_max_6024():
    assert max_6024(3, 7) == 7
