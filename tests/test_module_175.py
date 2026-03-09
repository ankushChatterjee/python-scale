"""Tests for test module 175 — covers src modules [697, 698, 699, 700]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_697 import add_697
from module_698 import subtract_698
from module_699 import multiply_699
from module_700 import divide_700

def test_add_697():
    assert add_697(2, 3) == 5

def test_subtract_698():
    assert subtract_698(10, 4) == 6

def test_multiply_699():
    assert multiply_699(3, 7) == 21

def test_divide_700():
    assert divide_700(10, 2) == 5.0
