"""Tests for module 105."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_105 import min_105, add_105, subtract_105, multiply_105

def test_min_105():
    assert min_105(3, 7) == 3

def test_add_105():
    assert add_105(2, 3) == 5

def test_subtract_105():
    assert subtract_105(10, 4) == 6

def test_multiply_105():
    assert multiply_105(3, 7) == 21
