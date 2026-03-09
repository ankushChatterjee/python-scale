"""Tests for test module 1311 — covers src modules [5241, 5242, 5243, 5244]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5241 import add_5241
from module_5242 import subtract_5242
from module_5243 import multiply_5243
from module_5244 import divide_5244

def test_add_5241():
    assert add_5241(2, 3) == 5

def test_subtract_5242():
    assert subtract_5242(10, 4) == 6

def test_multiply_5243():
    assert multiply_5243(3, 7) == 21

def test_divide_5244():
    assert divide_5244(10, 2) == 5.0
