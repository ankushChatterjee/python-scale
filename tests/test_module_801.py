"""Tests for test module 801 — covers src modules [3201, 3202, 3203, 3204]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3201 import add_3201
from module_3202 import subtract_3202
from module_3203 import multiply_3203
from module_3204 import divide_3204

def test_add_3201():
    assert add_3201(2, 3) == 5

def test_subtract_3202():
    assert subtract_3202(10, 4) == 6

def test_multiply_3203():
    assert multiply_3203(3, 7) == 21

def test_divide_3204():
    assert divide_3204(10, 2) == 5.0
