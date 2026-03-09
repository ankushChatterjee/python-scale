"""Tests for test module 1529 — covers src modules [6113, 6114, 6115, 6116]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6113 import add_6113
from module_6114 import subtract_6114
from module_6115 import multiply_6115
from module_6116 import divide_6116

def test_add_6113():
    assert add_6113(2, 3) == 5

def test_subtract_6114():
    assert subtract_6114(10, 4) == 6

def test_multiply_6115():
    assert multiply_6115(3, 7) == 21

def test_divide_6116():
    assert divide_6116(10, 2) == 5.0
