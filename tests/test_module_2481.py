"""Tests for test module 2481 — covers src modules [9921, 9922, 9923, 9924]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9921 import add_9921
from module_9922 import subtract_9922
from module_9923 import multiply_9923
from module_9924 import divide_9924

def test_add_9921():
    assert add_9921(2, 3) == 5

def test_subtract_9922():
    assert subtract_9922(10, 4) == 6

def test_multiply_9923():
    assert multiply_9923(3, 7) == 21

def test_divide_9924():
    assert divide_9924(10, 2) == 5.0
