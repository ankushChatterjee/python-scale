"""Tests for test module 2131 — covers src modules [8521, 8522, 8523, 8524]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8521 import add_8521
from module_8522 import subtract_8522
from module_8523 import multiply_8523
from module_8524 import divide_8524

def test_add_8521():
    assert add_8521(2, 3) == 5

def test_subtract_8522():
    assert subtract_8522(10, 4) == 6

def test_multiply_8523():
    assert multiply_8523(3, 7) == 21

def test_divide_8524():
    assert divide_8524(10, 2) == 5.0
