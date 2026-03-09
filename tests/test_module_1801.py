"""Tests for test module 1801 — covers src modules [7201, 7202, 7203, 7204]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7201 import add_7201
from module_7202 import subtract_7202
from module_7203 import multiply_7203
from module_7204 import divide_7204

def test_add_7201():
    assert add_7201(2, 3) == 5

def test_subtract_7202():
    assert subtract_7202(10, 4) == 6

def test_multiply_7203():
    assert multiply_7203(3, 7) == 21

def test_divide_7204():
    assert divide_7204(10, 2) == 5.0
