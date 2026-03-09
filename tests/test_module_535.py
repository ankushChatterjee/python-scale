"""Tests for test module 535 — covers src modules [2137, 2138, 2139, 2140]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2137 import add_2137
from module_2138 import subtract_2138
from module_2139 import multiply_2139
from module_2140 import divide_2140

def test_add_2137():
    assert add_2137(2, 3) == 5

def test_subtract_2138():
    assert subtract_2138(10, 4) == 6

def test_multiply_2139():
    assert multiply_2139(3, 7) == 21

def test_divide_2140():
    assert divide_2140(10, 2) == 5.0
