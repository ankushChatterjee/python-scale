"""Tests for test module 2127 — covers src modules [8505, 8506, 8507, 8508]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8505 import add_8505
from module_8506 import subtract_8506
from module_8507 import multiply_8507
from module_8508 import divide_8508

def test_add_8505():
    assert add_8505(2, 3) == 5

def test_subtract_8506():
    assert subtract_8506(10, 4) == 6

def test_multiply_8507():
    assert multiply_8507(3, 7) == 21

def test_divide_8508():
    assert divide_8508(10, 2) == 5.0
