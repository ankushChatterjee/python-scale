"""Tests for test module 1275 — covers src modules [5097, 5098, 5099, 5100]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5097 import add_5097
from module_5098 import subtract_5098
from module_5099 import multiply_5099
from module_5100 import divide_5100

def test_add_5097():
    assert add_5097(2, 3) == 5

def test_subtract_5098():
    assert subtract_5098(10, 4) == 6

def test_multiply_5099():
    assert multiply_5099(3, 7) == 21

def test_divide_5100():
    assert divide_5100(10, 2) == 5.0
