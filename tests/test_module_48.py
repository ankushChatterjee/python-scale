"""Tests for module 48."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_48 import modulo_48, divide_48, power_48, multiply_48

def test_modulo_48():
    assert modulo_48(10, 3) == 1

def test_divide_48():
    assert divide_48(10, 2) == 5.0

def test_power_48():
    assert power_48(2, 8) == 256

def test_multiply_48():
    assert multiply_48(3, 7) == 21
