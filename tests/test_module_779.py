"""Tests for test module 779 — covers src modules [3113, 3114, 3115, 3116]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3113 import add_3113
from module_3114 import subtract_3114
from module_3115 import multiply_3115
from module_3116 import divide_3116

def test_add_3113():
    assert add_3113(2, 3) == 5

def test_subtract_3114():
    assert subtract_3114(10, 4) == 6

def test_multiply_3115():
    assert multiply_3115(3, 7) == 21

def test_divide_3116():
    assert divide_3116(10, 2) == 5.0
