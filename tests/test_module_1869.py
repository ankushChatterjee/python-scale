"""Tests for test module 1869 — covers src modules [7473, 7474, 7475, 7476]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7473 import add_7473
from module_7474 import subtract_7474
from module_7475 import multiply_7475
from module_7476 import divide_7476

def test_add_7473():
    assert add_7473(2, 3) == 5

def test_subtract_7474():
    assert subtract_7474(10, 4) == 6

def test_multiply_7475():
    assert multiply_7475(3, 7) == 21

def test_divide_7476():
    assert divide_7476(10, 2) == 5.0
