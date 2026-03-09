"""Tests for test module 2285 — covers src modules [9137, 9138, 9139, 9140]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9137 import add_9137
from module_9138 import subtract_9138
from module_9139 import multiply_9139
from module_9140 import divide_9140

def test_add_9137():
    assert add_9137(2, 3) == 5

def test_subtract_9138():
    assert subtract_9138(10, 4) == 6

def test_multiply_9139():
    assert multiply_9139(3, 7) == 21

def test_divide_9140():
    assert divide_9140(10, 2) == 5.0
