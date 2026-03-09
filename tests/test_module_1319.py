"""Tests for test module 1319 — covers src modules [5273, 5274, 5275, 5276]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5273 import add_5273
from module_5274 import subtract_5274
from module_5275 import multiply_5275
from module_5276 import divide_5276

def test_add_5273():
    assert add_5273(2, 3) == 5

def test_subtract_5274():
    assert subtract_5274(10, 4) == 6

def test_multiply_5275():
    assert multiply_5275(3, 7) == 21

def test_divide_5276():
    assert divide_5276(10, 2) == 5.0
