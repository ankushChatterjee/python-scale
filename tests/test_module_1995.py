"""Tests for test module 1995 — covers src modules [7977, 7978, 7979, 7980]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7977 import add_7977
from module_7978 import subtract_7978
from module_7979 import multiply_7979
from module_7980 import divide_7980

def test_add_7977():
    assert add_7977(2, 3) == 5

def test_subtract_7978():
    assert subtract_7978(10, 4) == 6

def test_multiply_7979():
    assert multiply_7979(3, 7) == 21

def test_divide_7980():
    assert divide_7980(10, 2) == 5.0
