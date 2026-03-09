"""Tests for test module 2013 — covers src modules [8049, 8050, 8051, 8052]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8049 import add_8049
from module_8050 import subtract_8050
from module_8051 import multiply_8051
from module_8052 import divide_8052

def test_add_8049():
    assert add_8049(2, 3) == 5

def test_subtract_8050():
    assert subtract_8050(10, 4) == 6

def test_multiply_8051():
    assert multiply_8051(3, 7) == 21

def test_divide_8052():
    assert divide_8052(10, 2) == 5.0
