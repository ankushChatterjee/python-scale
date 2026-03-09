"""Tests for test module 1285 — covers src modules [5137, 5138, 5139, 5140]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5137 import add_5137
from module_5138 import subtract_5138
from module_5139 import multiply_5139
from module_5140 import divide_5140

def test_add_5137():
    assert add_5137(2, 3) == 5

def test_subtract_5138():
    assert subtract_5138(10, 4) == 6

def test_multiply_5139():
    assert multiply_5139(3, 7) == 21

def test_divide_5140():
    assert divide_5140(10, 2) == 5.0
