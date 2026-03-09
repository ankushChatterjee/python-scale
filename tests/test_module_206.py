"""Tests for module 206."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_206 import divide_206, multiply_206, subtract_206, min_206

def test_divide_206():
    assert divide_206(10, 2) == 5.0

def test_multiply_206():
    assert multiply_206(3, 7) == 21

def test_subtract_206():
    assert subtract_206(10, 4) == 6

def test_min_206():
    assert min_206(3, 7) == 3
