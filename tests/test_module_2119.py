"""Tests for test module 2119 — covers src modules [8473, 8474, 8475, 8476]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8473 import add_8473
from module_8474 import subtract_8474
from module_8475 import multiply_8475
from module_8476 import divide_8476

def test_add_8473():
    assert add_8473(2, 3) == 5

def test_subtract_8474():
    assert subtract_8474(10, 4) == 6

def test_multiply_8475():
    assert multiply_8475(3, 7) == 21

def test_divide_8476():
    assert divide_8476(10, 2) == 5.0
