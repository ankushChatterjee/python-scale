"""Tests for module 162."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_162 import multiply_162, min_162, divide_162, subtract_162

def test_multiply_162():
    assert multiply_162(3, 7) == 21

def test_min_162():
    assert min_162(3, 7) == 3

def test_divide_162():
    assert divide_162(10, 2) == 5.0

def test_subtract_162():
    assert subtract_162(10, 4) == 6
