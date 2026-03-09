"""Tests for test module 1817 — covers src modules [7265, 7266, 7267, 7268]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7265 import add_7265
from module_7266 import subtract_7266
from module_7267 import multiply_7267
from module_7268 import divide_7268

def test_add_7265():
    assert add_7265(2, 3) == 5

def test_subtract_7266():
    assert subtract_7266(10, 4) == 6

def test_multiply_7267():
    assert multiply_7267(3, 7) == 21

def test_divide_7268():
    assert divide_7268(10, 2) == 5.0
