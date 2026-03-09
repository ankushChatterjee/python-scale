"""Tests for test module 1257 — covers src modules [5025, 5026, 5027, 5028]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5025 import add_5025
from module_5026 import subtract_5026
from module_5027 import multiply_5027
from module_5028 import divide_5028

def test_add_5025():
    assert add_5025(2, 3) == 5

def test_subtract_5026():
    assert subtract_5026(10, 4) == 6

def test_multiply_5027():
    assert multiply_5027(3, 7) == 21

def test_divide_5028():
    assert divide_5028(10, 2) == 5.0
