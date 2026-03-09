"""Tests for test module 1483 — covers src modules [5929, 5930, 5931, 5932]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5929 import add_5929
from module_5930 import subtract_5930
from module_5931 import multiply_5931
from module_5932 import divide_5932

def test_add_5929():
    assert add_5929(2, 3) == 5

def test_subtract_5930():
    assert subtract_5930(10, 4) == 6

def test_multiply_5931():
    assert multiply_5931(3, 7) == 21

def test_divide_5932():
    assert divide_5932(10, 2) == 5.0
