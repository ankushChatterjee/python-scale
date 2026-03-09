"""Tests for test module 763 — covers src modules [3049, 3050, 3051, 3052]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3049 import add_3049
from module_3050 import subtract_3050
from module_3051 import multiply_3051
from module_3052 import divide_3052

def test_add_3049():
    assert add_3049(2, 3) == 5

def test_subtract_3050():
    assert subtract_3050(10, 4) == 6

def test_multiply_3051():
    assert multiply_3051(3, 7) == 21

def test_divide_3052():
    assert divide_3052(10, 2) == 5.0
