"""Tests for module 81."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_81 import divide_81, multiply_81, max_81, subtract_81

def test_divide_81():
    assert divide_81(10, 2) == 5.0

def test_multiply_81():
    assert multiply_81(3, 7) == 21

def test_max_81():
    assert max_81(3, 7) == 7

def test_subtract_81():
    assert subtract_81(10, 4) == 6
