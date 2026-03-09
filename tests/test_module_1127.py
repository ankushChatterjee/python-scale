"""Tests for test module 1127 — covers src modules [4505, 4506, 4507, 4508]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4505 import add_4505
from module_4506 import subtract_4506
from module_4507 import multiply_4507
from module_4508 import divide_4508

def test_add_4505():
    assert add_4505(2, 3) == 5

def test_subtract_4506():
    assert subtract_4506(10, 4) == 6

def test_multiply_4507():
    assert multiply_4507(3, 7) == 21

def test_divide_4508():
    assert divide_4508(10, 2) == 5.0
