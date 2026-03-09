"""Tests for test module 2211 — covers src modules [8841, 8842, 8843, 8844]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8841 import add_8841
from module_8842 import subtract_8842
from module_8843 import multiply_8843
from module_8844 import divide_8844

def test_add_8841():
    assert add_8841(2, 3) == 5

def test_subtract_8842():
    assert subtract_8842(10, 4) == 6

def test_multiply_8843():
    assert multiply_8843(3, 7) == 21

def test_divide_8844():
    assert divide_8844(10, 2) == 5.0
