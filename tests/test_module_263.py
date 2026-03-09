"""Tests for test module 263 — covers src modules [1049, 1050, 1051, 1052]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1049 import add_1049
from module_1050 import subtract_1050
from module_1051 import multiply_1051
from module_1052 import divide_1052

def test_add_1049():
    assert add_1049(2, 3) == 5

def test_subtract_1050():
    assert subtract_1050(10, 4) == 6

def test_multiply_1051():
    assert multiply_1051(3, 7) == 21

def test_divide_1052():
    assert divide_1052(10, 2) == 5.0
