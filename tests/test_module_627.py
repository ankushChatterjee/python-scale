"""Tests for test module 627 — covers src modules [2505, 2506, 2507, 2508]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2505 import add_2505
from module_2506 import subtract_2506
from module_2507 import multiply_2507
from module_2508 import divide_2508

def test_add_2505():
    assert add_2505(2, 3) == 5

def test_subtract_2506():
    assert subtract_2506(10, 4) == 6

def test_multiply_2507():
    assert multiply_2507(3, 7) == 21

def test_divide_2508():
    assert divide_2508(10, 2) == 5.0
