"""Tests for test module 1059 — covers src modules [4233, 4234, 4235, 4236]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4233 import add_4233
from module_4234 import subtract_4234
from module_4235 import multiply_4235
from module_4236 import divide_4236

def test_add_4233():
    assert add_4233(2, 3) == 5

def test_subtract_4234():
    assert subtract_4234(10, 4) == 6

def test_multiply_4235():
    assert multiply_4235(3, 7) == 21

def test_divide_4236():
    assert divide_4236(10, 2) == 5.0
