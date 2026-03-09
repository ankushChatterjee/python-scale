"""Tests for test module 1883 — covers src modules [7529, 7530, 7531, 7532]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7529 import add_7529
from module_7530 import subtract_7530
from module_7531 import multiply_7531
from module_7532 import divide_7532

def test_add_7529():
    assert add_7529(2, 3) == 5

def test_subtract_7530():
    assert subtract_7530(10, 4) == 6

def test_multiply_7531():
    assert multiply_7531(3, 7) == 21

def test_divide_7532():
    assert divide_7532(10, 2) == 5.0
