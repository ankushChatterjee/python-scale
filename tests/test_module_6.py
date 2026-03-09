"""Tests for module 6."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6 import min_6, subtract_6, divide_6, modulo_6

def test_min_6():
    assert min_6(3, 7) == 3

def test_subtract_6():
    assert subtract_6(10, 4) == 6

def test_divide_6():
    assert divide_6(10, 2) == 5.0

def test_modulo_6():
    assert modulo_6(10, 3) == 1
