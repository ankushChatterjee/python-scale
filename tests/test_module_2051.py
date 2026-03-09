"""Tests for test module 2051 — covers src modules [8201, 8202, 8203, 8204]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8201 import add_8201
from module_8202 import subtract_8202
from module_8203 import multiply_8203
from module_8204 import divide_8204

def test_add_8201():
    assert add_8201(2, 3) == 5

def test_subtract_8202():
    assert subtract_8202(10, 4) == 6

def test_multiply_8203():
    assert multiply_8203(3, 7) == 21

def test_divide_8204():
    assert divide_8204(10, 2) == 5.0
