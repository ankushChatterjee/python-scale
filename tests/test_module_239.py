"""Tests for test module 239 — covers src modules [953, 954, 955, 956]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_953 import add_953
from module_954 import subtract_954
from module_955 import multiply_955
from module_956 import divide_956

def test_add_953():
    assert add_953(2, 3) == 5

def test_subtract_954():
    assert subtract_954(10, 4) == 6

def test_multiply_955():
    assert multiply_955(3, 7) == 21

def test_divide_956():
    assert divide_956(10, 2) == 5.0
