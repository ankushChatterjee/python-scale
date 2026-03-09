"""Tests for test module 1025 — covers src modules [4097, 4098, 4099, 4100]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4097 import add_4097
from module_4098 import subtract_4098
from module_4099 import multiply_4099
from module_4100 import divide_4100

def test_add_4097():
    assert add_4097(2, 3) == 5

def test_subtract_4098():
    assert subtract_4098(10, 4) == 6

def test_multiply_4099():
    assert multiply_4099(3, 7) == 21

def test_divide_4100():
    assert divide_4100(10, 2) == 5.0
