"""Tests for test module 1759 — covers src modules [7033, 7034, 7035, 7036]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7033 import add_7033
from module_7034 import subtract_7034
from module_7035 import multiply_7035
from module_7036 import divide_7036

def test_add_7033():
    assert add_7033(2, 3) == 5

def test_subtract_7034():
    assert subtract_7034(10, 4) == 6

def test_multiply_7035():
    assert multiply_7035(3, 7) == 21

def test_divide_7036():
    assert divide_7036(10, 2) == 5.0
