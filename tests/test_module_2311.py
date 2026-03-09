"""Tests for test module 2311 — covers src modules [9241, 9242, 9243, 9244]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9241 import add_9241
from module_9242 import subtract_9242
from module_9243 import multiply_9243
from module_9244 import divide_9244

def test_add_9241():
    assert add_9241(2, 3) == 5

def test_subtract_9242():
    assert subtract_9242(10, 4) == 6

def test_multiply_9243():
    assert multiply_9243(3, 7) == 21

def test_divide_9244():
    assert divide_9244(10, 2) == 5.0
