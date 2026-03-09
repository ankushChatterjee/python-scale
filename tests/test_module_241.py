"""Tests for test module 241 — covers src modules [961, 962, 963, 964]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_961 import add_961
from module_962 import subtract_962
from module_963 import multiply_963
from module_964 import divide_964

def test_add_961():
    assert add_961(2, 3) == 5

def test_subtract_962():
    assert subtract_962(10, 4) == 6

def test_multiply_963():
    assert multiply_963(3, 7) == 21

def test_divide_964():
    assert divide_964(10, 2) == 5.0
