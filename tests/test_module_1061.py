"""Tests for test module 1061 — covers src modules [4241, 4242, 4243, 4244]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4241 import add_4241
from module_4242 import subtract_4242
from module_4243 import multiply_4243
from module_4244 import divide_4244

def test_add_4241():
    assert add_4241(2, 3) == 5

def test_subtract_4242():
    assert subtract_4242(10, 4) == 6

def test_multiply_4243():
    assert multiply_4243(3, 7) == 21

def test_divide_4244():
    assert divide_4244(10, 2) == 5.0
