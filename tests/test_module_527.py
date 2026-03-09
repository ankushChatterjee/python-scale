"""Tests for test module 527 — covers src modules [2105, 2106, 2107, 2108]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2105 import add_2105
from module_2106 import subtract_2106
from module_2107 import multiply_2107
from module_2108 import divide_2108

def test_add_2105():
    assert add_2105(2, 3) == 5

def test_subtract_2106():
    assert subtract_2106(10, 4) == 6

def test_multiply_2107():
    assert multiply_2107(3, 7) == 21

def test_divide_2108():
    assert divide_2108(10, 2) == 5.0
