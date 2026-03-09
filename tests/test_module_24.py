"""Tests for module 24."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_24 import min_24, multiply_24, add_24, subtract_24

def test_min_24():
    assert min_24(3, 7) == 3

def test_multiply_24():
    assert multiply_24(3, 7) == 21

def test_add_24():
    assert add_24(2, 3) == 5

def test_subtract_24():
    assert subtract_24(10, 4) == 6
