"""Tests for module 209."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_209 import modulo_209, power_209, subtract_209, divide_209

def test_modulo_209():
    assert modulo_209(10, 3) == 1

def test_power_209():
    assert power_209(2, 8) == 256

def test_subtract_209():
    assert subtract_209(10, 4) == 6

def test_divide_209():
    assert divide_209(10, 2) == 5.0
