"""Tests for test module 1209 — covers src modules [4833, 4834, 4835, 4836]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4833 import add_4833
from module_4834 import subtract_4834
from module_4835 import multiply_4835
from module_4836 import divide_4836

def test_add_4833():
    assert add_4833(2, 3) == 5

def test_subtract_4834():
    assert subtract_4834(10, 4) == 6

def test_multiply_4835():
    assert multiply_4835(3, 7) == 21

def test_divide_4836():
    assert divide_4836(10, 2) == 5.0
