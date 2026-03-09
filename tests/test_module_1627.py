"""Tests for test module 1627 — covers src modules [6505, 6506, 6507, 6508]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6505 import add_6505
from module_6506 import subtract_6506
from module_6507 import multiply_6507
from module_6508 import divide_6508

def test_add_6505():
    assert add_6505(2, 3) == 5

def test_subtract_6506():
    assert subtract_6506(10, 4) == 6

def test_multiply_6507():
    assert multiply_6507(3, 7) == 21

def test_divide_6508():
    assert divide_6508(10, 2) == 5.0
