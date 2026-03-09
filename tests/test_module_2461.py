"""Tests for test module 2461 — covers src modules [9841, 9842, 9843, 9844]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9841 import add_9841
from module_9842 import subtract_9842
from module_9843 import multiply_9843
from module_9844 import divide_9844

def test_add_9841():
    assert add_9841(2, 3) == 5

def test_subtract_9842():
    assert subtract_9842(10, 4) == 6

def test_multiply_9843():
    assert multiply_9843(3, 7) == 21

def test_divide_9844():
    assert divide_9844(10, 2) == 5.0
