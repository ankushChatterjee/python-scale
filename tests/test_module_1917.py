"""Tests for test module 1917 — covers src modules [7665, 7666, 7667, 7668]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7665 import add_7665
from module_7666 import subtract_7666
from module_7667 import multiply_7667
from module_7668 import divide_7668

def test_add_7665():
    assert add_7665(2, 3) == 5

def test_subtract_7666():
    assert subtract_7666(10, 4) == 6

def test_multiply_7667():
    assert multiply_7667(3, 7) == 21

def test_divide_7668():
    assert divide_7668(10, 2) == 5.0
