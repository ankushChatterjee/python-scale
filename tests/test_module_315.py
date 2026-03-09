"""Tests for test module 315 — covers src modules [1257, 1258, 1259, 1260]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1257 import add_1257
from module_1258 import subtract_1258
from module_1259 import multiply_1259
from module_1260 import divide_1260

def test_add_1257():
    assert add_1257(2, 3) == 5

def test_subtract_1258():
    assert subtract_1258(10, 4) == 6

def test_multiply_1259():
    assert multiply_1259(3, 7) == 21

def test_divide_1260():
    assert divide_1260(10, 2) == 5.0
