"""Tests for test module 1357 — covers src modules [5425, 5426, 5427, 5428]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5425 import add_5425
from module_5426 import subtract_5426
from module_5427 import multiply_5427
from module_5428 import divide_5428

def test_add_5425():
    assert add_5425(2, 3) == 5

def test_subtract_5426():
    assert subtract_5426(10, 4) == 6

def test_multiply_5427():
    assert multiply_5427(3, 7) == 21

def test_divide_5428():
    assert divide_5428(10, 2) == 5.0
