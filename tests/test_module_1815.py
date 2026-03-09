"""Tests for test module 1815 — covers src modules [7257, 7258, 7259, 7260]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7257 import add_7257
from module_7258 import subtract_7258
from module_7259 import multiply_7259
from module_7260 import divide_7260

def test_add_7257():
    assert add_7257(2, 3) == 5

def test_subtract_7258():
    assert subtract_7258(10, 4) == 6

def test_multiply_7259():
    assert multiply_7259(3, 7) == 21

def test_divide_7260():
    assert divide_7260(10, 2) == 5.0
