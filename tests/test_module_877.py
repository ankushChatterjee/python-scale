"""Tests for test module 877 — covers src modules [3505, 3506, 3507, 3508]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3505 import add_3505
from module_3506 import subtract_3506
from module_3507 import multiply_3507
from module_3508 import divide_3508

def test_add_3505():
    assert add_3505(2, 3) == 5

def test_subtract_3506():
    assert subtract_3506(10, 4) == 6

def test_multiply_3507():
    assert multiply_3507(3, 7) == 21

def test_divide_3508():
    assert divide_3508(10, 2) == 5.0
