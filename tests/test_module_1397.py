"""Tests for test module 1397 — covers src modules [5585, 5586, 5587, 5588]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5585 import add_5585
from module_5586 import subtract_5586
from module_5587 import multiply_5587
from module_5588 import divide_5588

def test_add_5585():
    assert add_5585(2, 3) == 5

def test_subtract_5586():
    assert subtract_5586(10, 4) == 6

def test_multiply_5587():
    assert multiply_5587(3, 7) == 21

def test_divide_5588():
    assert divide_5588(10, 2) == 5.0
