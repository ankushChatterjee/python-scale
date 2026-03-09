"""Tests for module 95."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_95 import add_95, multiply_95, subtract_95, min_95

def test_add_95():
    assert add_95(2, 3) == 5

def test_multiply_95():
    assert multiply_95(3, 7) == 21

def test_subtract_95():
    assert subtract_95(10, 4) == 6

def test_min_95():
    assert min_95(3, 7) == 3
