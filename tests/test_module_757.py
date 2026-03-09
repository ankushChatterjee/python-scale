"""Tests for test module 757 — covers src modules [3025, 3026, 3027, 3028]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3025 import add_3025
from module_3026 import subtract_3026
from module_3027 import multiply_3027
from module_3028 import divide_3028

def test_add_3025():
    assert add_3025(2, 3) == 5

def test_subtract_3026():
    assert subtract_3026(10, 4) == 6

def test_multiply_3027():
    assert multiply_3027(3, 7) == 21

def test_divide_3028():
    assert divide_3028(10, 2) == 5.0
