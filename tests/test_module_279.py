"""Tests for test module 279 — covers src modules [1113, 1114, 1115, 1116]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1113 import add_1113
from module_1114 import subtract_1114
from module_1115 import multiply_1115
from module_1116 import divide_1116

def test_add_1113():
    assert add_1113(2, 3) == 5

def test_subtract_1114():
    assert subtract_1114(10, 4) == 6

def test_multiply_1115():
    assert multiply_1115(3, 7) == 21

def test_divide_1116():
    assert divide_1116(10, 2) == 5.0
