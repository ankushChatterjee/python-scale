"""Tests for test module 1881 — covers src modules [7521, 7522, 7523, 7524]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7521 import add_7521
from module_7522 import subtract_7522
from module_7523 import multiply_7523
from module_7524 import divide_7524

def test_add_7521():
    assert add_7521(2, 3) == 5

def test_subtract_7522():
    assert subtract_7522(10, 4) == 6

def test_multiply_7523():
    assert multiply_7523(3, 7) == 21

def test_divide_7524():
    assert divide_7524(10, 2) == 5.0
