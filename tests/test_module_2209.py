"""Tests for test module 2209 — covers src modules [8833, 8834, 8835, 8836]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8833 import add_8833
from module_8834 import subtract_8834
from module_8835 import multiply_8835
from module_8836 import divide_8836

def test_add_8833():
    assert add_8833(2, 3) == 5

def test_subtract_8834():
    assert subtract_8834(10, 4) == 6

def test_multiply_8835():
    assert multiply_8835(3, 7) == 21

def test_divide_8836():
    assert divide_8836(10, 2) == 5.0
