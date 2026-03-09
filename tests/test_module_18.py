"""Tests for module 18."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_18 import multiply_18, max_18, min_18, subtract_18

def test_multiply_18():
    assert multiply_18(3, 7) == 21

def test_max_18():
    assert max_18(3, 7) == 7

def test_min_18():
    assert min_18(3, 7) == 3

def test_subtract_18():
    assert subtract_18(10, 4) == 6
