"""Tests for test module 1241 — covers src modules [4961, 4962, 4963, 4964]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4961 import add_4961
from module_4962 import subtract_4962
from module_4963 import multiply_4963
from module_4964 import divide_4964

def test_add_4961():
    assert add_4961(2, 3) == 5

def test_subtract_4962():
    assert subtract_4962(10, 4) == 6

def test_multiply_4963():
    assert multiply_4963(3, 7) == 21

def test_divide_4964():
    assert divide_4964(10, 2) == 5.0
