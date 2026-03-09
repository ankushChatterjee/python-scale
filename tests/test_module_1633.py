"""Tests for test module 1633 — covers src modules [6529, 6530, 6531, 6532]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6529 import add_6529
from module_6530 import subtract_6530
from module_6531 import multiply_6531
from module_6532 import divide_6532

def test_add_6529():
    assert add_6529(2, 3) == 5

def test_subtract_6530():
    assert subtract_6530(10, 4) == 6

def test_multiply_6531():
    assert multiply_6531(3, 7) == 21

def test_divide_6532():
    assert divide_6532(10, 2) == 5.0
