"""Tests for module 109."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_109 import divide_109, subtract_109, max_109, multiply_109

def test_divide_109():
    assert divide_109(10, 2) == 5.0

def test_subtract_109():
    assert subtract_109(10, 4) == 6

def test_max_109():
    assert max_109(3, 7) == 7

def test_multiply_109():
    assert multiply_109(3, 7) == 21
