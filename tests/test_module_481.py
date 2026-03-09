"""Tests for test module 481 — covers src modules [1921, 1922, 1923, 1924]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1921 import add_1921
from module_1922 import subtract_1922
from module_1923 import multiply_1923
from module_1924 import divide_1924

def test_add_1921():
    assert add_1921(2, 3) == 5

def test_subtract_1922():
    assert subtract_1922(10, 4) == 6

def test_multiply_1923():
    assert multiply_1923(3, 7) == 21

def test_divide_1924():
    assert divide_1924(10, 2) == 5.0
