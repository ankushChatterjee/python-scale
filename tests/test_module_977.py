"""Tests for test module 977 — covers src modules [3905, 3906, 3907, 3908]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3905 import add_3905
from module_3906 import subtract_3906
from module_3907 import multiply_3907
from module_3908 import divide_3908

def test_add_3905():
    assert add_3905(2, 3) == 5

def test_subtract_3906():
    assert subtract_3906(10, 4) == 6

def test_multiply_3907():
    assert multiply_3907(3, 7) == 21

def test_divide_3908():
    assert divide_3908(10, 2) == 5.0
