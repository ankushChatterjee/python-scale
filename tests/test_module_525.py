"""Tests for test module 525 — covers src modules [2097, 2098, 2099, 2100]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2097 import add_2097
from module_2098 import subtract_2098
from module_2099 import multiply_2099
from module_2100 import divide_2100

def test_add_2097():
    assert add_2097(2, 3) == 5

def test_subtract_2098():
    assert subtract_2098(10, 4) == 6

def test_multiply_2099():
    assert multiply_2099(3, 7) == 21

def test_divide_2100():
    assert divide_2100(10, 2) == 5.0
