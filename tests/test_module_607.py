"""Tests for test module 607 — covers src modules [2425, 2426, 2427, 2428]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2425 import add_2425
from module_2426 import subtract_2426
from module_2427 import multiply_2427
from module_2428 import divide_2428

def test_add_2425():
    assert add_2425(2, 3) == 5

def test_subtract_2426():
    assert subtract_2426(10, 4) == 6

def test_multiply_2427():
    assert multiply_2427(3, 7) == 21

def test_divide_2428():
    assert divide_2428(10, 2) == 5.0
