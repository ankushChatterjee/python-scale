"""Tests for test module 785 — covers src modules [3137, 3138, 3139, 3140]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3137 import add_3137
from module_3138 import subtract_3138
from module_3139 import multiply_3139
from module_3140 import divide_3140

def test_add_3137():
    assert add_3137(2, 3) == 5

def test_subtract_3138():
    assert subtract_3138(10, 4) == 6

def test_multiply_3139():
    assert multiply_3139(3, 7) == 21

def test_divide_3140():
    assert divide_3140(10, 2) == 5.0
