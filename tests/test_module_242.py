"""Tests for module 242."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_242 import max_242, multiply_242, divide_242, min_242

def test_max_242():
    assert max_242(3, 7) == 7

def test_multiply_242():
    assert multiply_242(3, 7) == 21

def test_divide_242():
    assert divide_242(10, 2) == 5.0

def test_min_242():
    assert min_242(3, 7) == 3
