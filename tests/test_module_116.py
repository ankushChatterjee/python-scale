"""Tests for module 116."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_116 import subtract_116, modulo_116, divide_116, multiply_116

def test_subtract_116():
    assert subtract_116(10, 4) == 6

def test_modulo_116():
    assert modulo_116(10, 3) == 1

def test_divide_116():
    assert divide_116(10, 2) == 5.0

def test_multiply_116():
    assert multiply_116(3, 7) == 21
