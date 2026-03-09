"""Tests for test module 1811 — covers src modules [7241, 7242, 7243, 7244]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7241 import add_7241
from module_7242 import subtract_7242
from module_7243 import multiply_7243
from module_7244 import divide_7244

def test_add_7241():
    assert add_7241(2, 3) == 5

def test_subtract_7242():
    assert subtract_7242(10, 4) == 6

def test_multiply_7243():
    assert multiply_7243(3, 7) == 21

def test_divide_7244():
    assert divide_7244(10, 2) == 5.0
