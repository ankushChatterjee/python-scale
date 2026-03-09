"""Tests for test module 1991 — covers src modules [7961, 7962, 7963, 7964]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7961 import add_7961
from module_7962 import subtract_7962
from module_7963 import multiply_7963
from module_7964 import divide_7964

def test_add_7961():
    assert add_7961(2, 3) == 5

def test_subtract_7962():
    assert subtract_7962(10, 4) == 6

def test_multiply_7963():
    assert multiply_7963(3, 7) == 21

def test_divide_7964():
    assert divide_7964(10, 2) == 5.0
