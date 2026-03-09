"""Tests for module 86."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_86 import divide_86, multiply_86, min_86, subtract_86

def test_divide_86():
    assert divide_86(10, 2) == 5.0

def test_multiply_86():
    assert multiply_86(3, 7) == 21

def test_min_86():
    assert min_86(3, 7) == 3

def test_subtract_86():
    assert subtract_86(10, 4) == 6
