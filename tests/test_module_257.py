"""Tests for test module 257 — covers src modules [1025, 1026, 1027, 1028]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1025 import add_1025
from module_1026 import subtract_1026
from module_1027 import multiply_1027
from module_1028 import divide_1028

def test_add_1025():
    assert add_1025(2, 3) == 5

def test_subtract_1026():
    assert subtract_1026(10, 4) == 6

def test_multiply_1027():
    assert multiply_1027(3, 7) == 21

def test_divide_1028():
    assert divide_1028(10, 2) == 5.0
