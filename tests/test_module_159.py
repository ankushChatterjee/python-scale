"""Tests for module 159."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_159 import multiply_159, min_159, divide_159, subtract_159

def test_multiply_159():
    assert multiply_159(3, 7) == 21

def test_min_159():
    assert min_159(3, 7) == 3

def test_divide_159():
    assert divide_159(10, 2) == 5.0

def test_subtract_159():
    assert subtract_159(10, 4) == 6
