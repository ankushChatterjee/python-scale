"""Tests for test module 639 — covers src modules [2553, 2554, 2555, 2556]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2553 import add_2553
from module_2554 import subtract_2554
from module_2555 import multiply_2555
from module_2556 import divide_2556

def test_add_2553():
    assert add_2553(2, 3) == 5

def test_subtract_2554():
    assert subtract_2554(10, 4) == 6

def test_multiply_2555():
    assert multiply_2555(3, 7) == 21

def test_divide_2556():
    assert divide_2556(10, 2) == 5.0
