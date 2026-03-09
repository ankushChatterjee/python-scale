"""Tests for module 234."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_234 import modulo_234, power_234, divide_234, multiply_234

def test_modulo_234():
    assert modulo_234(10, 3) == 1

def test_power_234():
    assert power_234(2, 8) == 256

def test_divide_234():
    assert divide_234(10, 2) == 5.0

def test_multiply_234():
    assert multiply_234(3, 7) == 21
