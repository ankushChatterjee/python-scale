"""Tests for test module 383 — covers src modules [1529, 1530, 1531, 1532]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1529 import add_1529
from module_1530 import subtract_1530
from module_1531 import multiply_1531
from module_1532 import divide_1532

def test_add_1529():
    assert add_1529(2, 3) == 5

def test_subtract_1530():
    assert subtract_1530(10, 4) == 6

def test_multiply_1531():
    assert multiply_1531(3, 7) == 21

def test_divide_1532():
    assert divide_1532(10, 2) == 5.0
