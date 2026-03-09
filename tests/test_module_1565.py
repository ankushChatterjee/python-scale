"""Tests for test module 1565 — covers src modules [6257, 6258, 6259, 6260]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6257 import add_6257
from module_6258 import subtract_6258
from module_6259 import multiply_6259
from module_6260 import divide_6260

def test_add_6257():
    assert add_6257(2, 3) == 5

def test_subtract_6258():
    assert subtract_6258(10, 4) == 6

def test_multiply_6259():
    assert multiply_6259(3, 7) == 21

def test_divide_6260():
    assert divide_6260(10, 2) == 5.0
