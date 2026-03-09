"""Tests for test module 1131 — covers src modules [4521, 4522, 4523, 4524]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4521 import add_4521
from module_4522 import subtract_4522
from module_4523 import multiply_4523
from module_4524 import divide_4524

def test_add_4521():
    assert add_4521(2, 3) == 5

def test_subtract_4522():
    assert subtract_4522(10, 4) == 6

def test_multiply_4523():
    assert multiply_4523(3, 7) == 21

def test_divide_4524():
    assert divide_4524(10, 2) == 5.0
