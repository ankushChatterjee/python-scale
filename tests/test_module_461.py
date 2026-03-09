"""Tests for test module 461 — covers src modules [1841, 1842, 1843, 1844]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1841 import add_1841
from module_1842 import subtract_1842
from module_1843 import multiply_1843
from module_1844 import divide_1844

def test_add_1841():
    assert add_1841(2, 3) == 5

def test_subtract_1842():
    assert subtract_1842(10, 4) == 6

def test_multiply_1843():
    assert multiply_1843(3, 7) == 21

def test_divide_1844():
    assert divide_1844(10, 2) == 5.0
