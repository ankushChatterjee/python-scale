"""Tests for test module 397 — covers src modules [1585, 1586, 1587, 1588]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1585 import add_1585
from module_1586 import subtract_1586
from module_1587 import multiply_1587
from module_1588 import divide_1588

def test_add_1585():
    assert add_1585(2, 3) == 5

def test_subtract_1586():
    assert subtract_1586(10, 4) == 6

def test_multiply_1587():
    assert multiply_1587(3, 7) == 21

def test_divide_1588():
    assert divide_1588(10, 2) == 5.0
