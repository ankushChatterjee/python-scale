"""Tests for module 170."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_170 import multiply_170, subtract_170, min_170, divide_170

def test_multiply_170():
    assert multiply_170(3, 7) == 21

def test_subtract_170():
    assert subtract_170(10, 4) == 6

def test_min_170():
    assert min_170(3, 7) == 3

def test_divide_170():
    assert divide_170(10, 2) == 5.0
