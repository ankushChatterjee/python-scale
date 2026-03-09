"""Tests for test module 567 — covers src modules [2265, 2266, 2267, 2268]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2265 import add_2265
from module_2266 import subtract_2266
from module_2267 import multiply_2267
from module_2268 import divide_2268

def test_add_2265():
    assert add_2265(2, 3) == 5

def test_subtract_2266():
    assert subtract_2266(10, 4) == 6

def test_multiply_2267():
    assert multiply_2267(3, 7) == 21

def test_divide_2268():
    assert divide_2268(10, 2) == 5.0
