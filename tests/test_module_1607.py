"""Tests for test module 1607 — covers src modules [6425, 6426, 6427, 6428]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6425 import add_6425
from module_6426 import subtract_6426
from module_6427 import multiply_6427
from module_6428 import divide_6428

def test_add_6425():
    assert add_6425(2, 3) == 5

def test_subtract_6426():
    assert subtract_6426(10, 4) == 6

def test_multiply_6427():
    assert multiply_6427(3, 7) == 21

def test_divide_6428():
    assert divide_6428(10, 2) == 5.0
