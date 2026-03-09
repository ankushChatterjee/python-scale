"""Tests for module 167."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_167 import add_167, multiply_167, subtract_167, max_167

def test_add_167():
    assert add_167(2, 3) == 5

def test_multiply_167():
    assert multiply_167(3, 7) == 21

def test_subtract_167():
    assert subtract_167(10, 4) == 6

def test_max_167():
    assert max_167(3, 7) == 7
