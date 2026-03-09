"""Tests for test module 301 — covers src modules [1201, 1202, 1203, 1204]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1201 import add_1201
from module_1202 import subtract_1202
from module_1203 import multiply_1203
from module_1204 import divide_1204

def test_add_1201():
    assert add_1201(2, 3) == 5

def test_subtract_1202():
    assert subtract_1202(10, 4) == 6

def test_multiply_1203():
    assert multiply_1203(3, 7) == 21

def test_divide_1204():
    assert divide_1204(10, 2) == 5.0
