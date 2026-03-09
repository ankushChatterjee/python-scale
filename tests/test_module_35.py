"""Tests for test module 35 — covers src modules [137, 138, 139, 140]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_137 import add_137
from module_138 import subtract_138
from module_139 import multiply_139
from module_140 import divide_140

def test_add_137():
    assert add_137(2, 3) == 5

def test_subtract_138():
    assert subtract_138(10, 4) == 6

def test_multiply_139():
    assert multiply_139(3, 7) == 21

def test_divide_140():
    assert divide_140(10, 2) == 5.0
