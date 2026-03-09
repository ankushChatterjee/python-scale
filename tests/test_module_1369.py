"""Tests for test module 1369 — covers src modules [5473, 5474, 5475, 5476]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5473 import add_5473
from module_5474 import subtract_5474
from module_5475 import multiply_5475
from module_5476 import divide_5476

def test_add_5473():
    assert add_5473(2, 3) == 5

def test_subtract_5474():
    assert subtract_5474(10, 4) == 6

def test_multiply_5475():
    assert multiply_5475(3, 7) == 21

def test_divide_5476():
    assert divide_5476(10, 2) == 5.0
