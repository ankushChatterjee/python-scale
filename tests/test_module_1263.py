"""Tests for test module 1263 — covers src modules [5049, 5050, 5051, 5052]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5049 import add_5049
from module_5050 import subtract_5050
from module_5051 import multiply_5051
from module_5052 import divide_5052

def test_add_5049():
    assert add_5049(2, 3) == 5

def test_subtract_5050():
    assert subtract_5050(10, 4) == 6

def test_multiply_5051():
    assert multiply_5051(3, 7) == 21

def test_divide_5052():
    assert divide_5052(10, 2) == 5.0
