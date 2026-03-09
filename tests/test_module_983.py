"""Tests for test module 983 — covers src modules [3929, 3930, 3931, 3932]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3929 import add_3929
from module_3930 import subtract_3930
from module_3931 import multiply_3931
from module_3932 import divide_3932

def test_add_3929():
    assert add_3929(2, 3) == 5

def test_subtract_3930():
    assert subtract_3930(10, 4) == 6

def test_multiply_3931():
    assert multiply_3931(3, 7) == 21

def test_divide_3932():
    assert divide_3932(10, 2) == 5.0
