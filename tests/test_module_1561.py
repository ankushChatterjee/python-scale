"""Tests for test module 1561 — covers src modules [6241, 6242, 6243, 6244]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6241 import add_6241
from module_6242 import subtract_6242
from module_6243 import multiply_6243
from module_6244 import divide_6244

def test_add_6241():
    assert add_6241(2, 3) == 5

def test_subtract_6242():
    assert subtract_6242(10, 4) == 6

def test_multiply_6243():
    assert multiply_6243(3, 7) == 21

def test_divide_6244():
    assert divide_6244(10, 2) == 5.0
