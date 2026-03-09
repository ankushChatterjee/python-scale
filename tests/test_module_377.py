"""Tests for test module 377 — covers src modules [1505, 1506, 1507, 1508]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1505 import add_1505
from module_1506 import subtract_1506
from module_1507 import multiply_1507
from module_1508 import divide_1508

def test_add_1505():
    assert add_1505(2, 3) == 5

def test_subtract_1506():
    assert subtract_1506(10, 4) == 6

def test_multiply_1507():
    assert multiply_1507(3, 7) == 21

def test_divide_1508():
    assert divide_1508(10, 2) == 5.0
