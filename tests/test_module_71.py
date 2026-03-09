"""Tests for module 71."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_71 import max_71, subtract_71, min_71, multiply_71

def test_max_71():
    assert max_71(3, 7) == 7

def test_subtract_71():
    assert subtract_71(10, 4) == 6

def test_min_71():
    assert min_71(3, 7) == 3

def test_multiply_71():
    assert multiply_71(3, 7) == 21
