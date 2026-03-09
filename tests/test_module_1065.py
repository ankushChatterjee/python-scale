"""Tests for test module 1065 — covers src modules [4257, 4258, 4259, 4260]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4257 import add_4257
from module_4258 import subtract_4258
from module_4259 import multiply_4259
from module_4260 import divide_4260

def test_add_4257():
    assert add_4257(2, 3) == 5

def test_subtract_4258():
    assert subtract_4258(10, 4) == 6

def test_multiply_4259():
    assert multiply_4259(3, 7) == 21

def test_divide_4260():
    assert divide_4260(10, 2) == 5.0
