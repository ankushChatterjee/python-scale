"""Tests for module 182."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_182 import subtract_182, divide_182, multiply_182, min_182

def test_subtract_182():
    assert subtract_182(10, 4) == 6

def test_divide_182():
    assert divide_182(10, 2) == 5.0

def test_multiply_182():
    assert multiply_182(3, 7) == 21

def test_min_182():
    assert min_182(3, 7) == 3
