"""Tests for test module 1809 — covers src modules [7233, 7234, 7235, 7236]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7233 import add_7233
from module_7234 import subtract_7234
from module_7235 import multiply_7235
from module_7236 import divide_7236

def test_add_7233():
    assert add_7233(2, 3) == 5

def test_subtract_7234():
    assert subtract_7234(10, 4) == 6

def test_multiply_7235():
    assert multiply_7235(3, 7) == 21

def test_divide_7236():
    assert divide_7236(10, 2) == 5.0
