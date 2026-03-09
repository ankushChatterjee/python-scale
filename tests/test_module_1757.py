"""Tests for test module 1757 — covers src modules [7025, 7026, 7027, 7028]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7025 import add_7025
from module_7026 import subtract_7026
from module_7027 import multiply_7027
from module_7028 import divide_7028

def test_add_7025():
    assert add_7025(2, 3) == 5

def test_subtract_7026():
    assert subtract_7026(10, 4) == 6

def test_multiply_7027():
    assert multiply_7027(3, 7) == 21

def test_divide_7028():
    assert divide_7028(10, 2) == 5.0
