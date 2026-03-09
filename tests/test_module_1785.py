"""Tests for test module 1785 — covers src modules [7137, 7138, 7139, 7140]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7137 import add_7137
from module_7138 import subtract_7138
from module_7139 import multiply_7139
from module_7140 import divide_7140

def test_add_7137():
    assert add_7137(2, 3) == 5

def test_subtract_7138():
    assert subtract_7138(10, 4) == 6

def test_multiply_7139():
    assert multiply_7139(3, 7) == 21

def test_divide_7140():
    assert divide_7140(10, 2) == 5.0
