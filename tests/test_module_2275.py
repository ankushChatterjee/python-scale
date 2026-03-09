"""Tests for test module 2275 — covers src modules [9097, 9098, 9099, 9100]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9097 import add_9097
from module_9098 import subtract_9098
from module_9099 import multiply_9099
from module_9100 import divide_9100

def test_add_9097():
    assert add_9097(2, 3) == 5

def test_subtract_9098():
    assert subtract_9098(10, 4) == 6

def test_multiply_9099():
    assert multiply_9099(3, 7) == 21

def test_divide_9100():
    assert divide_9100(10, 2) == 5.0
