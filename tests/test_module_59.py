"""Tests for test module 59 — covers src modules [233, 234, 235, 236]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_233 import add_233
from module_234 import subtract_234
from module_235 import multiply_235
from module_236 import divide_236

def test_add_233():
    assert add_233(2, 3) == 5

def test_subtract_234():
    assert subtract_234(10, 4) == 6

def test_multiply_235():
    assert multiply_235(3, 7) == 21

def test_divide_236():
    assert divide_236(10, 2) == 5.0
