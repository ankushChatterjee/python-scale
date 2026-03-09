"""Tests for test module 1449 — covers src modules [5793, 5794, 5795, 5796]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5793 import add_5793
from module_5794 import subtract_5794
from module_5795 import multiply_5795
from module_5796 import divide_5796

def test_add_5793():
    assert add_5793(2, 3) == 5

def test_subtract_5794():
    assert subtract_5794(10, 4) == 6

def test_multiply_5795():
    assert multiply_5795(3, 7) == 21

def test_divide_5796():
    assert divide_5796(10, 2) == 5.0
