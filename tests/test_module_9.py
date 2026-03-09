"""Tests for module 9."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9 import divide_9, min_9, multiply_9, add_9

def test_divide_9():
    assert divide_9(10, 2) == 5.0

def test_min_9():
    assert min_9(3, 7) == 3

def test_multiply_9():
    assert multiply_9(3, 7) == 21

def test_add_9():
    assert add_9(2, 3) == 5
