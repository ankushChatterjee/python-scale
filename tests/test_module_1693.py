"""Tests for test module 1693 — covers src modules [6769, 6770, 6771, 6772]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6769 import add_6769
from module_6770 import subtract_6770
from module_6771 import multiply_6771
from module_6772 import divide_6772

def test_add_6769():
    assert add_6769(2, 3) == 5

def test_subtract_6770():
    assert subtract_6770(10, 4) == 6

def test_multiply_6771():
    assert multiply_6771(3, 7) == 21

def test_divide_6772():
    assert divide_6772(10, 2) == 5.0
