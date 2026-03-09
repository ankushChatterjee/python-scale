"""Tests for test module 2309 — covers src modules [9233, 9234, 9235, 9236]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9233 import add_9233
from module_9234 import subtract_9234
from module_9235 import multiply_9235
from module_9236 import divide_9236

def test_add_9233():
    assert add_9233(2, 3) == 5

def test_subtract_9234():
    assert subtract_9234(10, 4) == 6

def test_multiply_9235():
    assert multiply_9235(3, 7) == 21

def test_divide_9236():
    assert divide_9236(10, 2) == 5.0
