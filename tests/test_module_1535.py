"""Tests for test module 1535 — covers src modules [6137, 6138, 6139, 6140]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6137 import add_6137
from module_6138 import subtract_6138
from module_6139 import multiply_6139
from module_6140 import divide_6140

def test_add_6137():
    assert add_6137(2, 3) == 5

def test_subtract_6138():
    assert subtract_6138(10, 4) == 6

def test_multiply_6139():
    assert multiply_6139(3, 7) == 21

def test_divide_6140():
    assert divide_6140(10, 2) == 5.0
