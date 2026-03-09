"""Tests for test module 1317 — covers src modules [5265, 5266, 5267, 5268]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5265 import add_5265
from module_5266 import subtract_5266
from module_5267 import multiply_5267
from module_5268 import divide_5268

def test_add_5265():
    assert add_5265(2, 3) == 5

def test_subtract_5266():
    assert subtract_5266(10, 4) == 6

def test_multiply_5267():
    assert multiply_5267(3, 7) == 21

def test_divide_5268():
    assert divide_5268(10, 2) == 5.0
