"""Tests for test module 127 — covers src modules [505, 506, 507, 508]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_505 import add_505
from module_506 import subtract_506
from module_507 import multiply_507
from module_508 import divide_508

def test_add_505():
    assert add_505(2, 3) == 5

def test_subtract_506():
    assert subtract_506(10, 4) == 6

def test_multiply_507():
    assert multiply_507(3, 7) == 21

def test_divide_508():
    assert divide_508(10, 2) == 5.0
