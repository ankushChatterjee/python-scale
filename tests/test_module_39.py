"""Tests for module 39."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_39 import divide_39, subtract_39, multiply_39, min_39

def test_divide_39():
    assert divide_39(10, 2) == 5.0

def test_subtract_39():
    assert subtract_39(10, 4) == 6

def test_multiply_39():
    assert multiply_39(3, 7) == 21

def test_min_39():
    assert min_39(3, 7) == 3
