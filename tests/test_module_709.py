"""Tests for test module 709 — covers src modules [2833, 2834, 2835, 2836]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2833 import add_2833
from module_2834 import subtract_2834
from module_2835 import multiply_2835
from module_2836 import divide_2836

def test_add_2833():
    assert add_2833(2, 3) == 5

def test_subtract_2834():
    assert subtract_2834(10, 4) == 6

def test_multiply_2835():
    assert multiply_2835(3, 7) == 21

def test_divide_2836():
    assert divide_2836(10, 2) == 5.0
