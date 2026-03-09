"""Tests for test module 2241 — covers src modules [8961, 8962, 8963, 8964]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8961 import add_8961
from module_8962 import subtract_8962
from module_8963 import multiply_8963
from module_8964 import divide_8964

def test_add_8961():
    assert add_8961(2, 3) == 5

def test_subtract_8962():
    assert subtract_8962(10, 4) == 6

def test_multiply_8963():
    assert multiply_8963(3, 7) == 21

def test_divide_8964():
    assert divide_8964(10, 2) == 5.0
