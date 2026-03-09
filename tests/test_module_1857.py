"""Tests for test module 1857 — covers src modules [7425, 7426, 7427, 7428]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7425 import add_7425
from module_7426 import subtract_7426
from module_7427 import multiply_7427
from module_7428 import divide_7428

def test_add_7425():
    assert add_7425(2, 3) == 5

def test_subtract_7426():
    assert subtract_7426(10, 4) == 6

def test_multiply_7427():
    assert multiply_7427(3, 7) == 21

def test_divide_7428():
    assert divide_7428(10, 2) == 5.0
