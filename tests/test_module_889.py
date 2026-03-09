"""Tests for test module 889 — covers src modules [3553, 3554, 3555, 3556]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3553 import add_3553
from module_3554 import subtract_3554
from module_3555 import multiply_3555
from module_3556 import divide_3556

def test_add_3553():
    assert add_3553(2, 3) == 5

def test_subtract_3554():
    assert subtract_3554(10, 4) == 6

def test_multiply_3555():
    assert multiply_3555(3, 7) == 21

def test_divide_3556():
    assert divide_3556(10, 2) == 5.0
