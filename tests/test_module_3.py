"""Tests for test module 3 — covers src modules [9, 10, 11, 12]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9 import add_9
from module_10 import subtract_10
from module_11 import multiply_11
from module_12 import divide_12

def test_add_9():
    assert add_9(2, 3) == 5

def test_subtract_10():
    assert subtract_10(10, 4) == 6

def test_multiply_11():
    assert multiply_11(3, 7) == 21

def test_divide_12():
    assert divide_12(10, 2) == 5.0
