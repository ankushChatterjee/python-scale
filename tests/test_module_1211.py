"""Tests for test module 1211 — covers src modules [4841, 4842, 4843, 4844]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4841 import add_4841
from module_4842 import subtract_4842
from module_4843 import multiply_4843
from module_4844 import divide_4844

def test_add_4841():
    assert add_4841(2, 3) == 5

def test_subtract_4842():
    assert subtract_4842(10, 4) == 6

def test_multiply_4843():
    assert multiply_4843(3, 7) == 21

def test_divide_4844():
    assert divide_4844(10, 2) == 5.0
