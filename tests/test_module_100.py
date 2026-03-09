"""Tests for module 100."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_100 import multiply_100, divide_100, subtract_100, add_100

def test_multiply_100():
    assert multiply_100(3, 7) == 21

def test_divide_100():
    assert divide_100(10, 2) == 5.0

def test_subtract_100():
    assert subtract_100(10, 4) == 6

def test_add_100():
    assert add_100(2, 3) == 5
