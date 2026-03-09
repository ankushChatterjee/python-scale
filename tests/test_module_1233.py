"""Tests for test module 1233 — covers src modules [4929, 4930, 4931, 4932]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4929 import add_4929
from module_4930 import subtract_4930
from module_4931 import multiply_4931
from module_4932 import divide_4932

def test_add_4929():
    assert add_4929(2, 3) == 5

def test_subtract_4930():
    assert subtract_4930(10, 4) == 6

def test_multiply_4931():
    assert multiply_4931(3, 7) == 21

def test_divide_4932():
    assert divide_4932(10, 2) == 5.0
