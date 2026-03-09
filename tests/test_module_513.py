"""Tests for test module 513 — covers src modules [2049, 2050, 2051, 2052]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2049 import add_2049
from module_2050 import subtract_2050
from module_2051 import multiply_2051
from module_2052 import divide_2052

def test_add_2049():
    assert add_2049(2, 3) == 5

def test_subtract_2050():
    assert subtract_2050(10, 4) == 6

def test_multiply_2051():
    assert multiply_2051(3, 7) == 21

def test_divide_2052():
    assert divide_2052(10, 2) == 5.0
