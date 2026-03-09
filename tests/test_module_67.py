"""Tests for test module 67 — covers src modules [265, 266, 267, 268]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_265 import add_265
from module_266 import subtract_266
from module_267 import multiply_267
from module_268 import divide_268

def test_add_265():
    assert add_265(2, 3) == 5

def test_subtract_266():
    assert subtract_266(10, 4) == 6

def test_multiply_267():
    assert multiply_267(3, 7) == 21

def test_divide_268():
    assert divide_268(10, 2) == 5.0
