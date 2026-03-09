"""Tests for test module 817 — covers src modules [3265, 3266, 3267, 3268]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3265 import add_3265
from module_3266 import subtract_3266
from module_3267 import multiply_3267
from module_3268 import divide_3268

def test_add_3265():
    assert add_3265(2, 3) == 5

def test_subtract_3266():
    assert subtract_3266(10, 4) == 6

def test_multiply_3267():
    assert multiply_3267(3, 7) == 21

def test_divide_3268():
    assert divide_3268(10, 2) == 5.0
