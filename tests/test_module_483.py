"""Tests for test module 483 — covers src modules [1929, 1930, 1931, 1932]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1929 import add_1929
from module_1930 import subtract_1930
from module_1931 import multiply_1931
from module_1932 import divide_1932

def test_add_1929():
    assert add_1929(2, 3) == 5

def test_subtract_1930():
    assert subtract_1930(10, 4) == 6

def test_multiply_1931():
    assert multiply_1931(3, 7) == 21

def test_divide_1932():
    assert divide_1932(10, 2) == 5.0
