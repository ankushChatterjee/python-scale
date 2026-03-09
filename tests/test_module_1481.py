"""Tests for test module 1481 — covers src modules [5921, 5922, 5923, 5924]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5921 import add_5921
from module_5922 import subtract_5922
from module_5923 import multiply_5923
from module_5924 import divide_5924

def test_add_5921():
    assert add_5921(2, 3) == 5

def test_subtract_5922():
    assert subtract_5922(10, 4) == 6

def test_multiply_5923():
    assert multiply_5923(3, 7) == 21

def test_divide_5924():
    assert divide_5924(10, 2) == 5.0
