"""Tests for test module 29 — covers src modules [113, 114, 115, 116]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_113 import add_113
from module_114 import subtract_114
from module_115 import multiply_115
from module_116 import divide_116

def test_add_113():
    assert add_113(2, 3) == 5

def test_subtract_114():
    assert subtract_114(10, 4) == 6

def test_multiply_115():
    assert multiply_115(3, 7) == 21

def test_divide_116():
    assert divide_116(10, 2) == 5.0
