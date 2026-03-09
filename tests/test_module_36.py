"""Tests for module 36."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_36 import subtract_36, multiply_36, divide_36, max_36

def test_subtract_36():
    assert subtract_36(10, 4) == 6

def test_multiply_36():
    assert multiply_36(3, 7) == 21

def test_divide_36():
    assert divide_36(10, 2) == 5.0

def test_max_36():
    assert max_36(3, 7) == 7
