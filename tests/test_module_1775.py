"""Tests for test module 1775 — covers src modules [7097, 7098, 7099, 7100]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7097 import add_7097
from module_7098 import subtract_7098
from module_7099 import multiply_7099
from module_7100 import divide_7100

def test_add_7097():
    assert add_7097(2, 3) == 5

def test_subtract_7098():
    assert subtract_7098(10, 4) == 6

def test_multiply_7099():
    assert multiply_7099(3, 7) == 21

def test_divide_7100():
    assert divide_7100(10, 2) == 5.0
