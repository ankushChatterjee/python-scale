"""Tests for module 17."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_17 import min_17, multiply_17, divide_17, max_17

def test_min_17():
    assert min_17(3, 7) == 3

def test_multiply_17():
    assert multiply_17(3, 7) == 21

def test_divide_17():
    assert divide_17(10, 2) == 5.0

def test_max_17():
    assert max_17(3, 7) == 7
