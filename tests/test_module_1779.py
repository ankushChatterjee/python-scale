"""Tests for test module 1779 — covers src modules [7113, 7114, 7115, 7116]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7113 import add_7113
from module_7114 import subtract_7114
from module_7115 import multiply_7115
from module_7116 import divide_7116

def test_add_7113():
    assert add_7113(2, 3) == 5

def test_subtract_7114():
    assert subtract_7114(10, 4) == 6

def test_multiply_7115():
    assert multiply_7115(3, 7) == 21

def test_divide_7116():
    assert divide_7116(10, 2) == 5.0
