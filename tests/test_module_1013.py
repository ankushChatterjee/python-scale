"""Tests for test module 1013 — covers src modules [4049, 4050, 4051, 4052]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4049 import add_4049
from module_4050 import subtract_4050
from module_4051 import multiply_4051
from module_4052 import divide_4052

def test_add_4049():
    assert add_4049(2, 3) == 5

def test_subtract_4050():
    assert subtract_4050(10, 4) == 6

def test_multiply_4051():
    assert multiply_4051(3, 7) == 21

def test_divide_4052():
    assert divide_4052(10, 2) == 5.0
