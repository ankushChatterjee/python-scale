"""Tests for test module 1007 — covers src modules [4025, 4026, 4027, 4028]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4025 import add_4025
from module_4026 import subtract_4026
from module_4027 import multiply_4027
from module_4028 import divide_4028

def test_add_4025():
    assert add_4025(2, 3) == 5

def test_subtract_4026():
    assert subtract_4026(10, 4) == 6

def test_multiply_4027():
    assert multiply_4027(3, 7) == 21

def test_divide_4028():
    assert divide_4028(10, 2) == 5.0
