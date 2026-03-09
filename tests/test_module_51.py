"""Tests for test module 51 — covers src modules [201, 202, 203, 204]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_201 import add_201
from module_202 import subtract_202
from module_203 import multiply_203
from module_204 import divide_204

def test_add_201():
    assert add_201(2, 3) == 5

def test_subtract_202():
    assert subtract_202(10, 4) == 6

def test_multiply_203():
    assert multiply_203(3, 7) == 21

def test_divide_204():
    assert divide_204(10, 2) == 5.0
