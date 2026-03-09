"""Tests for test module 959 — covers src modules [3833, 3834, 3835, 3836]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3833 import add_3833
from module_3834 import subtract_3834
from module_3835 import multiply_3835
from module_3836 import divide_3836

def test_add_3833():
    assert add_3833(2, 3) == 5

def test_subtract_3834():
    assert subtract_3834(10, 4) == 6

def test_multiply_3835():
    assert multiply_3835(3, 7) == 21

def test_divide_3836():
    assert divide_3836(10, 2) == 5.0
