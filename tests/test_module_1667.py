"""Tests for test module 1667 — covers src modules [6665, 6666, 6667, 6668]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6665 import add_6665
from module_6666 import subtract_6666
from module_6667 import multiply_6667
from module_6668 import divide_6668

def test_add_6665():
    assert add_6665(2, 3) == 5

def test_subtract_6666():
    assert subtract_6666(10, 4) == 6

def test_multiply_6667():
    assert multiply_6667(3, 7) == 21

def test_divide_6668():
    assert divide_6668(10, 2) == 5.0
