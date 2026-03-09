"""Tests for test module 1119 — covers src modules [4473, 4474, 4475, 4476]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4473 import add_4473
from module_4474 import subtract_4474
from module_4475 import multiply_4475
from module_4476 import divide_4476

def test_add_4473():
    assert add_4473(2, 3) == 5

def test_subtract_4474():
    assert subtract_4474(10, 4) == 6

def test_multiply_4475():
    assert multiply_4475(3, 7) == 21

def test_divide_4476():
    assert divide_4476(10, 2) == 5.0
