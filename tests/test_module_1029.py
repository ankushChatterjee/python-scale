"""Tests for test module 1029 — covers src modules [4113, 4114, 4115, 4116]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4113 import add_4113
from module_4114 import subtract_4114
from module_4115 import multiply_4115
from module_4116 import divide_4116

def test_add_4113():
    assert add_4113(2, 3) == 5

def test_subtract_4114():
    assert subtract_4114(10, 4) == 6

def test_multiply_4115():
    assert multiply_4115(3, 7) == 21

def test_divide_4116():
    assert divide_4116(10, 2) == 5.0
