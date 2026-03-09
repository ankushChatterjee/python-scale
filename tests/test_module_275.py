"""Tests for test module 275 — covers src modules [1097, 1098, 1099, 1100]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1097 import add_1097
from module_1098 import subtract_1098
from module_1099 import multiply_1099
from module_1100 import divide_1100

def test_add_1097():
    assert add_1097(2, 3) == 5

def test_subtract_1098():
    assert subtract_1098(10, 4) == 6

def test_multiply_1099():
    assert multiply_1099(3, 7) == 21

def test_divide_1100():
    assert divide_1100(10, 2) == 5.0
