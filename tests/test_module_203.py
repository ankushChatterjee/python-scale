"""Tests for module 203."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_203 import multiply_203, subtract_203, min_203, divide_203

def test_multiply_203():
    assert multiply_203(3, 7) == 21

def test_subtract_203():
    assert subtract_203(10, 4) == 6

def test_min_203():
    assert min_203(3, 7) == 3

def test_divide_203():
    assert divide_203(10, 2) == 5.0
