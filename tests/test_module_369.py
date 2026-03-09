"""Tests for test module 369 — covers src modules [1473, 1474, 1475, 1476]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1473 import add_1473
from module_1474 import subtract_1474
from module_1475 import multiply_1475
from module_1476 import divide_1476

def test_add_1473():
    assert add_1473(2, 3) == 5

def test_subtract_1474():
    assert subtract_1474(10, 4) == 6

def test_multiply_1475():
    assert multiply_1475(3, 7) == 21

def test_divide_1476():
    assert divide_1476(10, 2) == 5.0
