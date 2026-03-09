"""Tests for test module 1315 — covers src modules [5257, 5258, 5259, 5260]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5257 import add_5257
from module_5258 import subtract_5258
from module_5259 import multiply_5259
from module_5260 import divide_5260

def test_add_5257():
    assert add_5257(2, 3) == 5

def test_subtract_5258():
    assert subtract_5258(10, 4) == 6

def test_multiply_5259():
    assert multiply_5259(3, 7) == 21

def test_divide_5260():
    assert divide_5260(10, 2) == 5.0
