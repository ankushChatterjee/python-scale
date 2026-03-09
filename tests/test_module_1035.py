"""Tests for test module 1035 — covers src modules [4137, 4138, 4139, 4140]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4137 import add_4137
from module_4138 import subtract_4138
from module_4139 import multiply_4139
from module_4140 import divide_4140

def test_add_4137():
    assert add_4137(2, 3) == 5

def test_subtract_4138():
    assert subtract_4138(10, 4) == 6

def test_multiply_4139():
    assert multiply_4139(3, 7) == 21

def test_divide_4140():
    assert divide_4140(10, 2) == 5.0
