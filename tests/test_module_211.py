"""Tests for test module 211 — covers src modules [841, 842, 843, 844]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_841 import add_841
from module_842 import subtract_842
from module_843 import multiply_843
from module_844 import divide_844

def test_add_841():
    assert add_841(2, 3) == 5

def test_subtract_842():
    assert subtract_842(10, 4) == 6

def test_multiply_843():
    assert multiply_843(3, 7) == 21

def test_divide_844():
    assert divide_844(10, 2) == 5.0
