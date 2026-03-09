"""Tests for test module 619 — covers src modules [2473, 2474, 2475, 2476]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2473 import add_2473
from module_2474 import subtract_2474
from module_2475 import multiply_2475
from module_2476 import divide_2476

def test_add_2473():
    assert add_2473(2, 3) == 5

def test_subtract_2474():
    assert subtract_2474(10, 4) == 6

def test_multiply_2475():
    assert multiply_2475(3, 7) == 21

def test_divide_2476():
    assert divide_2476(10, 2) == 5.0
