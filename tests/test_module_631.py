"""Tests for test module 631 — covers src modules [2521, 2522, 2523, 2524]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2521 import add_2521
from module_2522 import subtract_2522
from module_2523 import multiply_2523
from module_2524 import divide_2524

def test_add_2521():
    assert add_2521(2, 3) == 5

def test_subtract_2522():
    assert subtract_2522(10, 4) == 6

def test_multiply_2523():
    assert multiply_2523(3, 7) == 21

def test_divide_2524():
    assert divide_2524(10, 2) == 5.0
