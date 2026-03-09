"""Tests for test module 37 — covers src modules [145, 146, 147, 148]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_145 import add_145
from module_146 import subtract_146
from module_147 import multiply_147
from module_148 import divide_148

def test_add_145():
    assert add_145(2, 3) == 5

def test_subtract_146():
    assert subtract_146(10, 4) == 6

def test_multiply_147():
    assert multiply_147(3, 7) == 21

def test_divide_148():
    assert divide_148(10, 2) == 5.0
