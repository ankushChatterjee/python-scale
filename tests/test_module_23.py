"""Tests for module 23."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_23 import divide_23, min_23, add_23, multiply_23

def test_divide_23():
    assert divide_23(10, 2) == 5.0

def test_min_23():
    assert min_23(3, 7) == 3

def test_add_23():
    assert add_23(2, 3) == 5

def test_multiply_23():
    assert multiply_23(3, 7) == 21
