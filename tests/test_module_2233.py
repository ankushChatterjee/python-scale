"""Tests for test module 2233 — covers src modules [8929, 8930, 8931, 8932]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8929 import add_8929
from module_8930 import subtract_8930
from module_8931 import multiply_8931
from module_8932 import divide_8932

def test_add_8929():
    assert add_8929(2, 3) == 5

def test_subtract_8930():
    assert subtract_8930(10, 4) == 6

def test_multiply_8931():
    assert multiply_8931(3, 7) == 21

def test_divide_8932():
    assert divide_8932(10, 2) == 5.0
