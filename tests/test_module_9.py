"""Tests for test module 9 — covers src modules [33, 34, 35, 36]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_33 import add_33
from module_34 import subtract_34
from module_35 import multiply_35
from module_36 import divide_36

def test_add_33():
    assert add_33(2, 3) == 5

def test_subtract_34():
    assert subtract_34(10, 4) == 6

def test_multiply_35():
    assert multiply_35(3, 7) == 21

def test_divide_36():
    assert divide_36(10, 2) == 5.0
