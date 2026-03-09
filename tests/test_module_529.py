"""Tests for test module 529 — covers src modules [2113, 2114, 2115, 2116]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2113 import add_2113
from module_2114 import subtract_2114
from module_2115 import multiply_2115
from module_2116 import divide_2116

def test_add_2113():
    assert add_2113(2, 3) == 5

def test_subtract_2114():
    assert subtract_2114(10, 4) == 6

def test_multiply_2115():
    assert multiply_2115(3, 7) == 21

def test_divide_2116():
    assert divide_2116(10, 2) == 5.0
