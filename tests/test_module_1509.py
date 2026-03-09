"""Tests for test module 1509 — covers src modules [6033, 6034, 6035, 6036]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6033 import add_6033
from module_6034 import subtract_6034
from module_6035 import multiply_6035
from module_6036 import divide_6036

def test_add_6033():
    assert add_6033(2, 3) == 5

def test_subtract_6034():
    assert subtract_6034(10, 4) == 6

def test_multiply_6035():
    assert multiply_6035(3, 7) == 21

def test_divide_6036():
    assert divide_6036(10, 2) == 5.0
