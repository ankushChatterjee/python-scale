"""Tests for test module 1647 — covers src modules [6585, 6586, 6587, 6588]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6585 import add_6585
from module_6586 import subtract_6586
from module_6587 import multiply_6587
from module_6588 import divide_6588

def test_add_6585():
    assert add_6585(2, 3) == 5

def test_subtract_6586():
    assert subtract_6586(10, 4) == 6

def test_multiply_6587():
    assert multiply_6587(3, 7) == 21

def test_divide_6588():
    assert divide_6588(10, 2) == 5.0
