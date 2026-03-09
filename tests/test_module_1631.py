"""Tests for test module 1631 — covers src modules [6521, 6522, 6523, 6524]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6521 import add_6521
from module_6522 import subtract_6522
from module_6523 import multiply_6523
from module_6524 import divide_6524

def test_add_6521():
    assert add_6521(2, 3) == 5

def test_subtract_6522():
    assert subtract_6522(10, 4) == 6

def test_multiply_6523():
    assert multiply_6523(3, 7) == 21

def test_divide_6524():
    assert divide_6524(10, 2) == 5.0
