"""Tests for test module 1381 — covers src modules [5521, 5522, 5523, 5524]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5521 import add_5521
from module_5522 import subtract_5522
from module_5523 import multiply_5523
from module_5524 import divide_5524

def test_add_5521():
    assert add_5521(2, 3) == 5

def test_subtract_5522():
    assert subtract_5522(10, 4) == 6

def test_multiply_5523():
    assert multiply_5523(3, 7) == 21

def test_divide_5524():
    assert divide_5524(10, 2) == 5.0
