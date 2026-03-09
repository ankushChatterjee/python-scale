"""Tests for test module 2027 — covers src modules [8105, 8106, 8107, 8108]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8105 import add_8105
from module_8106 import subtract_8106
from module_8107 import multiply_8107
from module_8108 import divide_8108

def test_add_8105():
    assert add_8105(2, 3) == 5

def test_subtract_8106():
    assert subtract_8106(10, 4) == 6

def test_multiply_8107():
    assert multiply_8107(3, 7) == 21

def test_divide_8108():
    assert divide_8108(10, 2) == 5.0
