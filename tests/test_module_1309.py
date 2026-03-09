"""Tests for test module 1309 — covers src modules [5233, 5234, 5235, 5236]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5233 import add_5233
from module_5234 import subtract_5234
from module_5235 import multiply_5235
from module_5236 import divide_5236

def test_add_5233():
    assert add_5233(2, 3) == 5

def test_subtract_5234():
    assert subtract_5234(10, 4) == 6

def test_multiply_5235():
    assert multiply_5235(3, 7) == 21

def test_divide_5236():
    assert divide_5236(10, 2) == 5.0
