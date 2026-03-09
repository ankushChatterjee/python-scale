"""Tests for test module 1619 — covers src modules [6473, 6474, 6475, 6476]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6473 import add_6473
from module_6474 import subtract_6474
from module_6475 import multiply_6475
from module_6476 import divide_6476

def test_add_6473():
    assert add_6473(2, 3) == 5

def test_subtract_6474():
    assert subtract_6474(10, 4) == 6

def test_multiply_6475():
    assert multiply_6475(3, 7) == 21

def test_divide_6476():
    assert divide_6476(10, 2) == 5.0
