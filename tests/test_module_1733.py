"""Tests for test module 1733 — covers src modules [6929, 6930, 6931, 6932]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6929 import add_6929
from module_6930 import subtract_6930
from module_6931 import multiply_6931
from module_6932 import divide_6932

def test_add_6929():
    assert add_6929(2, 3) == 5

def test_subtract_6930():
    assert subtract_6930(10, 4) == 6

def test_multiply_6931():
    assert multiply_6931(3, 7) == 21

def test_divide_6932():
    assert divide_6932(10, 2) == 5.0
