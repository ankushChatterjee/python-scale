"""Tests for test module 1383 — covers src modules [5529, 5530, 5531, 5532]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5529 import add_5529
from module_5530 import subtract_5530
from module_5531 import multiply_5531
from module_5532 import divide_5532

def test_add_5529():
    assert add_5529(2, 3) == 5

def test_subtract_5530():
    assert subtract_5530(10, 4) == 6

def test_multiply_5531():
    assert multiply_5531(3, 7) == 21

def test_divide_5532():
    assert divide_5532(10, 2) == 5.0
