"""Tests for test module 131 — covers src modules [521, 522, 523, 524]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_521 import add_521
from module_522 import subtract_522
from module_523 import multiply_523
from module_524 import divide_524

def test_add_521():
    assert add_521(2, 3) == 5

def test_subtract_522():
    assert subtract_522(10, 4) == 6

def test_multiply_523():
    assert multiply_523(3, 7) == 21

def test_divide_524():
    assert divide_524(10, 2) == 5.0
