"""Tests for module 213."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_213 import max_213, add_213, min_213, divide_213

def test_max_213():
    assert max_213(3, 7) == 7

def test_add_213():
    assert add_213(2, 3) == 5

def test_min_213():
    assert min_213(3, 7) == 3

def test_divide_213():
    assert divide_213(10, 2) == 5.0
