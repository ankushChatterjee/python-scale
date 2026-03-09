"""Tests for test module 809 — covers src modules [3233, 3234, 3235, 3236]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3233 import add_3233
from module_3234 import subtract_3234
from module_3235 import multiply_3235
from module_3236 import divide_3236

def test_add_3233():
    assert add_3233(2, 3) == 5

def test_subtract_3234():
    assert subtract_3234(10, 4) == 6

def test_multiply_3235():
    assert multiply_3235(3, 7) == 21

def test_divide_3236():
    assert divide_3236(10, 2) == 5.0
