"""Tests for test module 119 — covers src modules [473, 474, 475, 476]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_473 import add_473
from module_474 import subtract_474
from module_475 import multiply_475
from module_476 import divide_476

def test_add_473():
    assert add_473(2, 3) == 5

def test_subtract_474():
    assert subtract_474(10, 4) == 6

def test_multiply_475():
    assert multiply_475(3, 7) == 21

def test_divide_476():
    assert divide_476(10, 2) == 5.0
