"""Tests for test module 1559 — covers src modules [6233, 6234, 6235, 6236]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6233 import add_6233
from module_6234 import subtract_6234
from module_6235 import multiply_6235
from module_6236 import divide_6236

def test_add_6233():
    assert add_6233(2, 3) == 5

def test_subtract_6234():
    assert subtract_6234(10, 4) == 6

def test_multiply_6235():
    assert multiply_6235(3, 7) == 21

def test_divide_6236():
    assert divide_6236(10, 2) == 5.0
