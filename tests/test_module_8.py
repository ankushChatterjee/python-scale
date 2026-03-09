"""Tests for module 8."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8 import min_8, multiply_8, max_8, subtract_8

def test_min_8():
    assert min_8(3, 7) == 3

def test_multiply_8():
    assert multiply_8(3, 7) == 21

def test_max_8():
    assert max_8(3, 7) == 7

def test_subtract_8():
    assert subtract_8(10, 4) == 6
