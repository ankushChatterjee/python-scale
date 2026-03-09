"""Tests for test module 559 — covers src modules [2233, 2234, 2235, 2236]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2233 import add_2233
from module_2234 import subtract_2234
from module_2235 import multiply_2235
from module_2236 import divide_2236

def test_add_2233():
    assert add_2233(2, 3) == 5

def test_subtract_2234():
    assert subtract_2234(10, 4) == 6

def test_multiply_2235():
    assert multiply_2235(3, 7) == 21

def test_divide_2236():
    assert divide_2236(10, 2) == 5.0
