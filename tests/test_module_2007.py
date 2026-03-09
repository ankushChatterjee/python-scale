"""Tests for test module 2007 — covers src modules [8025, 8026, 8027, 8028]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8025 import add_8025
from module_8026 import subtract_8026
from module_8027 import multiply_8027
from module_8028 import divide_8028

def test_add_8025():
    assert add_8025(2, 3) == 5

def test_subtract_8026():
    assert subtract_8026(10, 4) == 6

def test_multiply_8027():
    assert multiply_8027(3, 7) == 21

def test_divide_8028():
    assert divide_8028(10, 2) == 5.0
