"""Tests for test module 2369 — covers src modules [9473, 9474, 9475, 9476]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9473 import add_9473
from module_9474 import subtract_9474
from module_9475 import multiply_9475
from module_9476 import divide_9476

def test_add_9473():
    assert add_9473(2, 3) == 5

def test_subtract_9474():
    assert subtract_9474(10, 4) == 6

def test_multiply_9475():
    assert multiply_9475(3, 7) == 21

def test_divide_9476():
    assert divide_9476(10, 2) == 5.0
