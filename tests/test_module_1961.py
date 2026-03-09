"""Tests for test module 1961 — covers src modules [7841, 7842, 7843, 7844]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7841 import add_7841
from module_7842 import subtract_7842
from module_7843 import multiply_7843
from module_7844 import divide_7844

def test_add_7841():
    assert add_7841(2, 3) == 5

def test_subtract_7842():
    assert subtract_7842(10, 4) == 6

def test_multiply_7843():
    assert multiply_7843(3, 7) == 21

def test_divide_7844():
    assert divide_7844(10, 2) == 5.0
