"""Tests for test module 1731 — covers src modules [6921, 6922, 6923, 6924]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6921 import add_6921
from module_6922 import subtract_6922
from module_6923 import multiply_6923
from module_6924 import divide_6924

def test_add_6921():
    assert add_6921(2, 3) == 5

def test_subtract_6922():
    assert subtract_6922(10, 4) == 6

def test_multiply_6923():
    assert multiply_6923(3, 7) == 21

def test_divide_6924():
    assert divide_6924(10, 2) == 5.0
