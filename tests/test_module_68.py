"""Tests for module 68."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_68 import min_68, add_68, subtract_68, divide_68

def test_min_68():
    assert min_68(3, 7) == 3

def test_add_68():
    assert add_68(2, 3) == 5

def test_subtract_68():
    assert subtract_68(10, 4) == 6

def test_divide_68():
    assert divide_68(10, 2) == 5.0
