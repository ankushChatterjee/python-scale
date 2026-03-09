"""Tests for module 21."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_21 import multiply_21, divide_21, min_21, max_21

def test_multiply_21():
    assert multiply_21(3, 7) == 21

def test_divide_21():
    assert divide_21(10, 2) == 5.0

def test_min_21():
    assert min_21(3, 7) == 3

def test_max_21():
    assert max_21(3, 7) == 7
