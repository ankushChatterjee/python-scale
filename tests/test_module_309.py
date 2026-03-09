"""Tests for test module 309 — covers src modules [1233, 1234, 1235, 1236]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1233 import add_1233
from module_1234 import subtract_1234
from module_1235 import multiply_1235
from module_1236 import divide_1236

def test_add_1233():
    assert add_1233(2, 3) == 5

def test_subtract_1234():
    assert subtract_1234(10, 4) == 6

def test_multiply_1235():
    assert multiply_1235(3, 7) == 21

def test_divide_1236():
    assert divide_1236(10, 2) == 5.0
