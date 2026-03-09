"""Tests for test module 1287 — covers src modules [5145, 5146, 5147, 5148]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5145 import add_5145
from module_5146 import subtract_5146
from module_5147 import multiply_5147
from module_5148 import divide_5148

def test_add_5145():
    assert add_5145(2, 3) == 5

def test_subtract_5146():
    assert subtract_5146(10, 4) == 6

def test_multiply_5147():
    assert multiply_5147(3, 7) == 21

def test_divide_5148():
    assert divide_5148(10, 2) == 5.0
