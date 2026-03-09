"""Tests for test module 2059 — covers src modules [8233, 8234, 8235, 8236]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8233 import add_8233
from module_8234 import subtract_8234
from module_8235 import multiply_8235
from module_8236 import divide_8236

def test_add_8233():
    assert add_8233(2, 3) == 5

def test_subtract_8234():
    assert subtract_8234(10, 4) == 6

def test_multiply_8235():
    assert multiply_8235(3, 7) == 21

def test_divide_8236():
    assert divide_8236(10, 2) == 5.0
