"""Tests for test module 1709 — covers src modules [6833, 6834, 6835, 6836]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6833 import add_6833
from module_6834 import subtract_6834
from module_6835 import multiply_6835
from module_6836 import divide_6836

def test_add_6833():
    assert add_6833(2, 3) == 5

def test_subtract_6834():
    assert subtract_6834(10, 4) == 6

def test_multiply_6835():
    assert multiply_6835(3, 7) == 21

def test_divide_6836():
    assert divide_6836(10, 2) == 5.0
