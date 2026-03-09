"""Tests for test module 1699 — covers src modules [6793, 6794, 6795, 6796]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6793 import add_6793
from module_6794 import subtract_6794
from module_6795 import multiply_6795
from module_6796 import divide_6796

def test_add_6793():
    assert add_6793(2, 3) == 5

def test_subtract_6794():
    assert subtract_6794(10, 4) == 6

def test_multiply_6795():
    assert multiply_6795(3, 7) == 21

def test_divide_6796():
    assert divide_6796(10, 2) == 5.0
