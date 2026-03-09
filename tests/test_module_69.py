"""Tests for module 69."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_69 import add_69, divide_69, multiply_69, min_69

def test_add_69():
    assert add_69(2, 3) == 5

def test_divide_69():
    assert divide_69(10, 2) == 5.0

def test_multiply_69():
    assert multiply_69(3, 7) == 21

def test_min_69():
    assert min_69(3, 7) == 3
