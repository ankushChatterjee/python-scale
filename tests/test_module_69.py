"""Tests for test module 69 — covers src modules [273, 274, 275, 276]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_273 import add_273
from module_274 import subtract_274
from module_275 import multiply_275
from module_276 import divide_276

def test_add_273():
    assert add_273(2, 3) == 5

def test_subtract_274():
    assert subtract_274(10, 4) == 6

def test_multiply_275():
    assert multiply_275(3, 7) == 21

def test_divide_276():
    assert divide_276(10, 2) == 5.0
