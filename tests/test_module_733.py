"""Tests for test module 733 — covers src modules [2929, 2930, 2931, 2932]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2929 import add_2929
from module_2930 import subtract_2930
from module_2931 import multiply_2931
from module_2932 import divide_2932

def test_add_2929():
    assert add_2929(2, 3) == 5

def test_subtract_2930():
    assert subtract_2930(10, 4) == 6

def test_multiply_2931():
    assert multiply_2931(3, 7) == 21

def test_divide_2932():
    assert divide_2932(10, 2) == 5.0
