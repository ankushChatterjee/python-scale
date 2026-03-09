"""Tests for test module 1819 — covers src modules [7273, 7274, 7275, 7276]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7273 import add_7273
from module_7274 import subtract_7274
from module_7275 import multiply_7275
from module_7276 import divide_7276

def test_add_7273():
    assert add_7273(2, 3) == 5

def test_subtract_7274():
    assert subtract_7274(10, 4) == 6

def test_multiply_7275():
    assert multiply_7275(3, 7) == 21

def test_divide_7276():
    assert divide_7276(10, 2) == 5.0
