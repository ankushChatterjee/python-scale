"""Tests for test module 285 — covers src modules [1137, 1138, 1139, 1140]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1137 import add_1137
from module_1138 import subtract_1138
from module_1139 import multiply_1139
from module_1140 import divide_1140

def test_add_1137():
    assert add_1137(2, 3) == 5

def test_subtract_1138():
    assert subtract_1138(10, 4) == 6

def test_multiply_1139():
    assert multiply_1139(3, 7) == 21

def test_divide_1140():
    assert divide_1140(10, 2) == 5.0
