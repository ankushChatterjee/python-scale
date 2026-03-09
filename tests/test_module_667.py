"""Tests for test module 667 — covers src modules [2665, 2666, 2667, 2668]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2665 import add_2665
from module_2666 import subtract_2666
from module_2667 import multiply_2667
from module_2668 import divide_2668

def test_add_2665():
    assert add_2665(2, 3) == 5

def test_subtract_2666():
    assert subtract_2666(10, 4) == 6

def test_multiply_2667():
    assert multiply_2667(3, 7) == 21

def test_divide_2668():
    assert divide_2668(10, 2) == 5.0
