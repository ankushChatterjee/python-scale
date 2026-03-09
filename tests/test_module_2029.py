"""Tests for test module 2029 — covers src modules [8113, 8114, 8115, 8116]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8113 import add_8113
from module_8114 import subtract_8114
from module_8115 import multiply_8115
from module_8116 import divide_8116

def test_add_8113():
    assert add_8113(2, 3) == 5

def test_subtract_8114():
    assert subtract_8114(10, 4) == 6

def test_multiply_8115():
    assert multiply_8115(3, 7) == 21

def test_divide_8116():
    assert divide_8116(10, 2) == 5.0
