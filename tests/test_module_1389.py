"""Tests for test module 1389 — covers src modules [5553, 5554, 5555, 5556]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5553 import add_5553
from module_5554 import subtract_5554
from module_5555 import multiply_5555
from module_5556 import divide_5556

def test_add_5553():
    assert add_5553(2, 3) == 5

def test_subtract_5554():
    assert subtract_5554(10, 4) == 6

def test_multiply_5555():
    assert multiply_5555(3, 7) == 21

def test_divide_5556():
    assert divide_5556(10, 2) == 5.0
