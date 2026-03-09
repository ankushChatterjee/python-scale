"""Tests for test module 917 — covers src modules [3665, 3666, 3667, 3668]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3665 import add_3665
from module_3666 import subtract_3666
from module_3667 import multiply_3667
from module_3668 import divide_3668

def test_add_3665():
    assert add_3665(2, 3) == 5

def test_subtract_3666():
    assert subtract_3666(10, 4) == 6

def test_multiply_3667():
    assert multiply_3667(3, 7) == 21

def test_divide_3668():
    assert divide_3668(10, 2) == 5.0
