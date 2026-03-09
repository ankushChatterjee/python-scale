"""Tests for test module 1981 — covers src modules [7921, 7922, 7923, 7924]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7921 import add_7921
from module_7922 import subtract_7922
from module_7923 import multiply_7923
from module_7924 import divide_7924

def test_add_7921():
    assert add_7921(2, 3) == 5

def test_subtract_7922():
    assert subtract_7922(10, 4) == 6

def test_multiply_7923():
    assert multiply_7923(3, 7) == 21

def test_divide_7924():
    assert divide_7924(10, 2) == 5.0
