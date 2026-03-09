"""Tests for test module 815 — covers src modules [3257, 3258, 3259, 3260]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3257 import add_3257
from module_3258 import subtract_3258
from module_3259 import multiply_3259
from module_3260 import divide_3260

def test_add_3257():
    assert add_3257(2, 3) == 5

def test_subtract_3258():
    assert subtract_3258(10, 4) == 6

def test_multiply_3259():
    assert multiply_3259(3, 7) == 21

def test_divide_3260():
    assert divide_3260(10, 2) == 5.0
