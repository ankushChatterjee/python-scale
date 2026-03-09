"""Tests for test module 1139 — covers src modules [4553, 4554, 4555, 4556]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4553 import add_4553
from module_4554 import subtract_4554
from module_4555 import multiply_4555
from module_4556 import divide_4556

def test_add_4553():
    assert add_4553(2, 3) == 5

def test_subtract_4554():
    assert subtract_4554(10, 4) == 6

def test_multiply_4555():
    assert multiply_4555(3, 7) == 21

def test_divide_4556():
    assert divide_4556(10, 2) == 5.0
