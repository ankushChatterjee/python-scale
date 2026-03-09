"""Tests for test module 2061 — covers src modules [8241, 8242, 8243, 8244]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8241 import add_8241
from module_8242 import subtract_8242
from module_8243 import multiply_8243
from module_8244 import divide_8244

def test_add_8241():
    assert add_8241(2, 3) == 5

def test_subtract_8242():
    assert subtract_8242(10, 4) == 6

def test_multiply_8243():
    assert multiply_8243(3, 7) == 21

def test_divide_8244():
    assert divide_8244(10, 2) == 5.0
