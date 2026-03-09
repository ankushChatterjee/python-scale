"""Tests for test module 1567 — covers src modules [6265, 6266, 6267, 6268]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6265 import add_6265
from module_6266 import subtract_6266
from module_6267 import multiply_6267
from module_6268 import divide_6268

def test_add_6265():
    assert add_6265(2, 3) == 5

def test_subtract_6266():
    assert subtract_6266(10, 4) == 6

def test_multiply_6267():
    assert multiply_6267(3, 7) == 21

def test_divide_6268():
    assert divide_6268(10, 2) == 5.0
