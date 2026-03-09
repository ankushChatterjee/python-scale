"""Tests for test module 1551 — covers src modules [6201, 6202, 6203, 6204]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6201 import add_6201
from module_6202 import subtract_6202
from module_6203 import multiply_6203
from module_6204 import divide_6204

def test_add_6201():
    assert add_6201(2, 3) == 5

def test_subtract_6202():
    assert subtract_6202(10, 4) == 6

def test_multiply_6203():
    assert multiply_6203(3, 7) == 21

def test_divide_6204():
    assert divide_6204(10, 2) == 5.0
