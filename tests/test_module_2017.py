"""Tests for test module 2017 — covers src modules [8065, 8066, 8067, 8068]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8065 import add_8065
from module_8066 import subtract_8066
from module_8067 import multiply_8067
from module_8068 import divide_8068

def test_add_8065():
    assert add_8065(2, 3) == 5

def test_subtract_8066():
    assert subtract_8066(10, 4) == 6

def test_multiply_8067():
    assert multiply_8067(3, 7) == 21

def test_divide_8068():
    assert divide_8068(10, 2) == 5.0
