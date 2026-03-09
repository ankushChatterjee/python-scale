"""Tests for test module 883 — covers src modules [3529, 3530, 3531, 3532]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3529 import add_3529
from module_3530 import subtract_3530
from module_3531 import multiply_3531
from module_3532 import divide_3532

def test_add_3529():
    assert add_3529(2, 3) == 5

def test_subtract_3530():
    assert subtract_3530(10, 4) == 6

def test_multiply_3531():
    assert multiply_3531(3, 7) == 21

def test_divide_3532():
    assert divide_3532(10, 2) == 5.0
