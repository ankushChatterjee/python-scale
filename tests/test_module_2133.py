"""Tests for test module 2133 — covers src modules [8529, 8530, 8531, 8532]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8529 import add_8529
from module_8530 import subtract_8530
from module_8531 import multiply_8531
from module_8532 import divide_8532

def test_add_8529():
    assert add_8529(2, 3) == 5

def test_subtract_8530():
    assert subtract_8530(10, 4) == 6

def test_multiply_8531():
    assert multiply_8531(3, 7) == 21

def test_divide_8532():
    assert divide_8532(10, 2) == 5.0
