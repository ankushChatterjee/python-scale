"""Tests for test module 1459 — covers src modules [5833, 5834, 5835, 5836]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5833 import add_5833
from module_5834 import subtract_5834
from module_5835 import multiply_5835
from module_5836 import divide_5836

def test_add_5833():
    assert add_5833(2, 3) == 5

def test_subtract_5834():
    assert subtract_5834(10, 4) == 6

def test_multiply_5835():
    assert multiply_5835(3, 7) == 21

def test_divide_5836():
    assert divide_5836(10, 2) == 5.0
