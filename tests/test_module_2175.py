"""Tests for test module 2175 — covers src modules [8697, 8698, 8699, 8700]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8697 import add_8697
from module_8698 import subtract_8698
from module_8699 import multiply_8699
from module_8700 import divide_8700

def test_add_8697():
    assert add_8697(2, 3) == 5

def test_subtract_8698():
    assert subtract_8698(10, 4) == 6

def test_multiply_8699():
    assert multiply_8699(3, 7) == 21

def test_divide_8700():
    assert divide_8700(10, 2) == 5.0
