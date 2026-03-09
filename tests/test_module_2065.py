"""Tests for test module 2065 — covers src modules [8257, 8258, 8259, 8260]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8257 import add_8257
from module_8258 import subtract_8258
from module_8259 import multiply_8259
from module_8260 import divide_8260

def test_add_8257():
    assert add_8257(2, 3) == 5

def test_subtract_8258():
    assert subtract_8258(10, 4) == 6

def test_multiply_8259():
    assert multiply_8259(3, 7) == 21

def test_divide_8260():
    assert divide_8260(10, 2) == 5.0
