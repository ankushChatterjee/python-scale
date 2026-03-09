"""Tests for test module 531 — covers src modules [2121, 2122, 2123, 2124]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2121 import add_2121
from module_2122 import subtract_2122
from module_2123 import multiply_2123
from module_2124 import divide_2124

def test_add_2121():
    assert add_2121(2, 3) == 5

def test_subtract_2122():
    assert subtract_2122(10, 4) == 6

def test_multiply_2123():
    assert multiply_2123(3, 7) == 21

def test_divide_2124():
    assert divide_2124(10, 2) == 5.0
