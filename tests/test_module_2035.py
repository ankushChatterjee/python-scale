"""Tests for test module 2035 — covers src modules [8137, 8138, 8139, 8140]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8137 import add_8137
from module_8138 import subtract_8138
from module_8139 import multiply_8139
from module_8140 import divide_8140

def test_add_8137():
    assert add_8137(2, 3) == 5

def test_subtract_8138():
    assert subtract_8138(10, 4) == 6

def test_multiply_8139():
    assert multiply_8139(3, 7) == 21

def test_divide_8140():
    assert divide_8140(10, 2) == 5.0
