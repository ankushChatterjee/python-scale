"""Tests for test module 2357 — covers src modules [9425, 9426, 9427, 9428]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9425 import add_9425
from module_9426 import subtract_9426
from module_9427 import multiply_9427
from module_9428 import divide_9428

def test_add_9425():
    assert add_9425(2, 3) == 5

def test_subtract_9426():
    assert subtract_9426(10, 4) == 6

def test_multiply_9427():
    assert multiply_9427(3, 7) == 21

def test_divide_9428():
    assert divide_9428(10, 2) == 5.0
