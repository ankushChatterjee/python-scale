"""Tests for module 151."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_151 import subtract_151, divide_151, min_151, multiply_151

def test_subtract_151():
    assert subtract_151(10, 4) == 6

def test_divide_151():
    assert divide_151(10, 2) == 5.0

def test_min_151():
    assert min_151(3, 7) == 3

def test_multiply_151():
    assert multiply_151(3, 7) == 21
