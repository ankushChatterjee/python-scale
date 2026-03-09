"""Tests for module 141."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_141 import subtract_141, divide_141, max_141, min_141

def test_subtract_141():
    assert subtract_141(10, 4) == 6

def test_divide_141():
    assert divide_141(10, 2) == 5.0

def test_max_141():
    assert max_141(3, 7) == 7

def test_min_141():
    assert min_141(3, 7) == 3
