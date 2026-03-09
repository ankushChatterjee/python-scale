"""Tests for module 2."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2 import divide_2, subtract_2, min_2, add_2

def test_divide_2():
    assert divide_2(10, 2) == 5.0

def test_subtract_2():
    assert subtract_2(10, 4) == 6

def test_min_2():
    assert min_2(3, 7) == 3

def test_add_2():
    assert add_2(2, 3) == 5
