"""Tests for test module 1673 — covers src modules [6689, 6690, 6691, 6692]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6689 import add_6689
from module_6690 import subtract_6690
from module_6691 import multiply_6691
from module_6692 import divide_6692

def test_add_6689():
    assert add_6689(2, 3) == 5

def test_subtract_6690():
    assert subtract_6690(10, 4) == 6

def test_multiply_6691():
    assert multiply_6691(3, 7) == 21

def test_divide_6692():
    assert divide_6692(10, 2) == 5.0
