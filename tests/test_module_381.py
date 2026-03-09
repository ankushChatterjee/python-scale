"""Tests for test module 381 — covers src modules [1521, 1522, 1523, 1524]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1521 import add_1521
from module_1522 import subtract_1522
from module_1523 import multiply_1523
from module_1524 import divide_1524

def test_add_1521():
    assert add_1521(2, 3) == 5

def test_subtract_1522():
    assert subtract_1522(10, 4) == 6

def test_multiply_1523():
    assert multiply_1523(3, 7) == 21

def test_divide_1524():
    assert divide_1524(10, 2) == 5.0
