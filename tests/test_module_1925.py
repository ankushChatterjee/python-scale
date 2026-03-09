"""Tests for test module 1925 — covers src modules [7697, 7698, 7699, 7700]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7697 import add_7697
from module_7698 import subtract_7698
from module_7699 import multiply_7699
from module_7700 import divide_7700

def test_add_7697():
    assert add_7697(2, 3) == 5

def test_subtract_7698():
    assert subtract_7698(10, 4) == 6

def test_multiply_7699():
    assert multiply_7699(3, 7) == 21

def test_divide_7700():
    assert divide_7700(10, 2) == 5.0
