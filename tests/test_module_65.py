"""Tests for test module 65 — covers src modules [257, 258, 259, 260]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_257 import add_257
from module_258 import subtract_258
from module_259 import multiply_259
from module_260 import divide_260

def test_add_257():
    assert add_257(2, 3) == 5

def test_subtract_258():
    assert subtract_258(10, 4) == 6

def test_multiply_259():
    assert multiply_259(3, 7) == 21

def test_divide_260():
    assert divide_260(10, 2) == 5.0
