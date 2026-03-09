"""Tests for test module 2231 — covers src modules [8921, 8922, 8923, 8924]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8921 import add_8921
from module_8922 import subtract_8922
from module_8923 import multiply_8923
from module_8924 import divide_8924

def test_add_8921():
    assert add_8921(2, 3) == 5

def test_subtract_8922():
    assert subtract_8922(10, 4) == 6

def test_multiply_8923():
    assert multiply_8923(3, 7) == 21

def test_divide_8924():
    assert divide_8924(10, 2) == 5.0
