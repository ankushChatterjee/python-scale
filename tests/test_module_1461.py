"""Tests for test module 1461 — covers src modules [5841, 5842, 5843, 5844]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5841 import add_5841
from module_5842 import subtract_5842
from module_5843 import multiply_5843
from module_5844 import divide_5844

def test_add_5841():
    assert add_5841(2, 3) == 5

def test_subtract_5842():
    assert subtract_5842(10, 4) == 6

def test_multiply_5843():
    assert multiply_5843(3, 7) == 21

def test_divide_5844():
    assert divide_5844(10, 2) == 5.0
