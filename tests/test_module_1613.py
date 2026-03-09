"""Tests for test module 1613 — covers src modules [6449, 6450, 6451, 6452]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6449 import add_6449
from module_6450 import subtract_6450
from module_6451 import multiply_6451
from module_6452 import divide_6452

def test_add_6449():
    assert add_6449(2, 3) == 5

def test_subtract_6450():
    assert subtract_6450(10, 4) == 6

def test_multiply_6451():
    assert multiply_6451(3, 7) == 21

def test_divide_6452():
    assert divide_6452(10, 2) == 5.0
