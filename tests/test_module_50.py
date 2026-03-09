"""Tests for module 50."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_50 import divide_50, subtract_50, add_50, multiply_50

def test_divide_50():
    assert divide_50(10, 2) == 5.0

def test_subtract_50():
    assert subtract_50(10, 4) == 6

def test_add_50():
    assert add_50(2, 3) == 5

def test_multiply_50():
    assert multiply_50(3, 7) == 21
