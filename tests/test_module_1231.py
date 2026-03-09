"""Tests for test module 1231 — covers src modules [4921, 4922, 4923, 4924]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4921 import add_4921
from module_4922 import subtract_4922
from module_4923 import multiply_4923
from module_4924 import divide_4924

def test_add_4921():
    assert add_4921(2, 3) == 5

def test_subtract_4922():
    assert subtract_4922(10, 4) == 6

def test_multiply_4923():
    assert multiply_4923(3, 7) == 21

def test_divide_4924():
    assert divide_4924(10, 2) == 5.0
