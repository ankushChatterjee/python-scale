"""Tests for test module 1279 — covers src modules [5113, 5114, 5115, 5116]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5113 import add_5113
from module_5114 import subtract_5114
from module_5115 import multiply_5115
from module_5116 import divide_5116

def test_add_5113():
    assert add_5113(2, 3) == 5

def test_subtract_5114():
    assert subtract_5114(10, 4) == 6

def test_multiply_5115():
    assert multiply_5115(3, 7) == 21

def test_divide_5116():
    assert divide_5116(10, 2) == 5.0
