"""Tests for test module 1983 — covers src modules [7929, 7930, 7931, 7932]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7929 import add_7929
from module_7930 import subtract_7930
from module_7931 import multiply_7931
from module_7932 import divide_7932

def test_add_7929():
    assert add_7929(2, 3) == 5

def test_subtract_7930():
    assert subtract_7930(10, 4) == 6

def test_multiply_7931():
    assert multiply_7931(3, 7) == 21

def test_divide_7932():
    assert divide_7932(10, 2) == 5.0
