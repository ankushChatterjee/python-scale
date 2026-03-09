"""Tests for module 79."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_79 import subtract_79, divide_79, power_79, modulo_79

def test_subtract_79():
    assert subtract_79(10, 4) == 6

def test_divide_79():
    assert divide_79(10, 2) == 5.0

def test_power_79():
    assert power_79(2, 8) == 256

def test_modulo_79():
    assert modulo_79(10, 3) == 1
