"""Tests for test module 1417 — covers src modules [5665, 5666, 5667, 5668]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5665 import add_5665
from module_5666 import subtract_5666
from module_5667 import multiply_5667
from module_5668 import divide_5668

def test_add_5665():
    assert add_5665(2, 3) == 5

def test_subtract_5666():
    assert subtract_5666(10, 4) == 6

def test_multiply_5667():
    assert multiply_5667(3, 7) == 21

def test_divide_5668():
    assert divide_5668(10, 2) == 5.0
