"""Tests for test module 1051 — covers src modules [4201, 4202, 4203, 4204]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4201 import add_4201
from module_4202 import subtract_4202
from module_4203 import multiply_4203
from module_4204 import divide_4204

def test_add_4201():
    assert add_4201(2, 3) == 5

def test_subtract_4202():
    assert subtract_4202(10, 4) == 6

def test_multiply_4203():
    assert multiply_4203(3, 7) == 21

def test_divide_4204():
    assert divide_4204(10, 2) == 5.0
