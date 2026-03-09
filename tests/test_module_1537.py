"""Tests for test module 1537 — covers src modules [6145, 6146, 6147, 6148]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6145 import add_6145
from module_6146 import subtract_6146
from module_6147 import multiply_6147
from module_6148 import divide_6148

def test_add_6145():
    assert add_6145(2, 3) == 5

def test_subtract_6146():
    assert subtract_6146(10, 4) == 6

def test_multiply_6147():
    assert multiply_6147(3, 7) == 21

def test_divide_6148():
    assert divide_6148(10, 2) == 5.0
