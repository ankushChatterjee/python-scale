"""Tests for test module 561 — covers src modules [2241, 2242, 2243, 2244]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2241 import add_2241
from module_2242 import subtract_2242
from module_2243 import multiply_2243
from module_2244 import divide_2244

def test_add_2241():
    assert add_2241(2, 3) == 5

def test_subtract_2242():
    assert subtract_2242(10, 4) == 6

def test_multiply_2243():
    assert multiply_2243(3, 7) == 21

def test_divide_2244():
    assert divide_2244(10, 2) == 5.0
