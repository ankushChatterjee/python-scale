"""Tests for test module 1745 — covers src modules [6977, 6978, 6979, 6980]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6977 import add_6977
from module_6978 import subtract_6978
from module_6979 import multiply_6979
from module_6980 import divide_6980

def test_add_6977():
    assert add_6977(2, 3) == 5

def test_subtract_6978():
    assert subtract_6978(10, 4) == 6

def test_multiply_6979():
    assert multiply_6979(3, 7) == 21

def test_divide_6980():
    assert divide_6980(10, 2) == 5.0
