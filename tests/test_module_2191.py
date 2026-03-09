"""Tests for test module 2191 — covers src modules [8761, 8762, 8763, 8764]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8761 import add_8761
from module_8762 import subtract_8762
from module_8763 import multiply_8763
from module_8764 import divide_8764

def test_add_8761():
    assert add_8761(2, 3) == 5

def test_subtract_8762():
    assert subtract_8762(10, 4) == 6

def test_multiply_8763():
    assert multiply_8763(3, 7) == 21

def test_divide_8764():
    assert divide_8764(10, 2) == 5.0
