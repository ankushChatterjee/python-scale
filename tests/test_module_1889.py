"""Tests for test module 1889 — covers src modules [7553, 7554, 7555, 7556]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7553 import add_7553
from module_7554 import subtract_7554
from module_7555 import multiply_7555
from module_7556 import divide_7556

def test_add_7553():
    assert add_7553(2, 3) == 5

def test_subtract_7554():
    assert subtract_7554(10, 4) == 6

def test_multiply_7555():
    assert multiply_7555(3, 7) == 21

def test_divide_7556():
    assert divide_7556(10, 2) == 5.0
