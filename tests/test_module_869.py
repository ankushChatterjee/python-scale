"""Tests for test module 869 — covers src modules [3473, 3474, 3475, 3476]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3473 import add_3473
from module_3474 import subtract_3474
from module_3475 import multiply_3475
from module_3476 import divide_3476

def test_add_3473():
    assert add_3473(2, 3) == 5

def test_subtract_3474():
    assert subtract_3474(10, 4) == 6

def test_multiply_3475():
    assert multiply_3475(3, 7) == 21

def test_divide_3476():
    assert divide_3476(10, 2) == 5.0
