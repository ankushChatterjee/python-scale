"""Tests for test module 1727 — covers src modules [6905, 6906, 6907, 6908]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6905 import add_6905
from module_6906 import subtract_6906
from module_6907 import multiply_6907
from module_6908 import divide_6908

def test_add_6905():
    assert add_6905(2, 3) == 5

def test_subtract_6906():
    assert subtract_6906(10, 4) == 6

def test_multiply_6907():
    assert multiply_6907(3, 7) == 21

def test_divide_6908():
    assert divide_6908(10, 2) == 5.0
