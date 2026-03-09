"""Tests for test module 1491 — covers src modules [5961, 5962, 5963, 5964]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5961 import add_5961
from module_5962 import subtract_5962
from module_5963 import multiply_5963
from module_5964 import divide_5964

def test_add_5961():
    assert add_5961(2, 3) == 5

def test_subtract_5962():
    assert subtract_5962(10, 4) == 6

def test_multiply_5963():
    assert multiply_5963(3, 7) == 21

def test_divide_5964():
    assert divide_5964(10, 2) == 5.0
