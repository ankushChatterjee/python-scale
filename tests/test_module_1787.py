"""Tests for test module 1787 — covers src modules [7145, 7146, 7147, 7148]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7145 import add_7145
from module_7146 import subtract_7146
from module_7147 import multiply_7147
from module_7148 import divide_7148

def test_add_7145():
    assert add_7145(2, 3) == 5

def test_subtract_7146():
    assert subtract_7146(10, 4) == 6

def test_multiply_7147():
    assert multiply_7147(3, 7) == 21

def test_divide_7148():
    assert divide_7148(10, 2) == 5.0
