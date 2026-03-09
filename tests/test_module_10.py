"""Tests for module 10."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_10 import subtract_10, divide_10, add_10, multiply_10

def test_subtract_10():
    assert subtract_10(10, 4) == 6

def test_divide_10():
    assert divide_10(10, 2) == 5.0

def test_add_10():
    assert add_10(2, 3) == 5

def test_multiply_10():
    assert multiply_10(3, 7) == 21
