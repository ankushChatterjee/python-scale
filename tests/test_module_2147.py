"""Tests for test module 2147 — covers src modules [8585, 8586, 8587, 8588]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8585 import add_8585
from module_8586 import subtract_8586
from module_8587 import multiply_8587
from module_8588 import divide_8588

def test_add_8585():
    assert add_8585(2, 3) == 5

def test_subtract_8586():
    assert subtract_8586(10, 4) == 6

def test_multiply_8587():
    assert multiply_8587(3, 7) == 21

def test_divide_8588():
    assert divide_8588(10, 2) == 5.0
