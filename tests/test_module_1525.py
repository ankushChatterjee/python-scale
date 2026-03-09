"""Tests for test module 1525 — covers src modules [6097, 6098, 6099, 6100]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6097 import add_6097
from module_6098 import subtract_6098
from module_6099 import multiply_6099
from module_6100 import divide_6100

def test_add_6097():
    assert add_6097(2, 3) == 5

def test_subtract_6098():
    assert subtract_6098(10, 4) == 6

def test_multiply_6099():
    assert multiply_6099(3, 7) == 21

def test_divide_6100():
    assert divide_6100(10, 2) == 5.0
