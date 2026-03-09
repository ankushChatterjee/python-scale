"""Tests for test module 491 — covers src modules [1961, 1962, 1963, 1964]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1961 import add_1961
from module_1962 import subtract_1962
from module_1963 import multiply_1963
from module_1964 import divide_1964

def test_add_1961():
    assert add_1961(2, 3) == 5

def test_subtract_1962():
    assert subtract_1962(10, 4) == 6

def test_multiply_1963():
    assert multiply_1963(3, 7) == 21

def test_divide_1964():
    assert divide_1964(10, 2) == 5.0
