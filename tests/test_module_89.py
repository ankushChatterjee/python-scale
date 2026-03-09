"""Tests for module 89."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_89 import subtract_89, max_89, multiply_89, add_89

def test_subtract_89():
    assert subtract_89(10, 4) == 6

def test_max_89():
    assert max_89(3, 7) == 7

def test_multiply_89():
    assert multiply_89(3, 7) == 21

def test_add_89():
    assert add_89(2, 3) == 5
