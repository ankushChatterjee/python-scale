"""Tests for test module 1653 — covers src modules [6609, 6610, 6611, 6612]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6609 import add_6609
from module_6610 import subtract_6610
from module_6611 import multiply_6611
from module_6612 import divide_6612

def test_add_6609():
    assert add_6609(2, 3) == 5

def test_subtract_6610():
    assert subtract_6610(10, 4) == 6

def test_multiply_6611():
    assert multiply_6611(3, 7) == 21

def test_divide_6612():
    assert divide_6612(10, 2) == 5.0
