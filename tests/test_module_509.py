"""Tests for test module 509 — covers src modules [2033, 2034, 2035, 2036]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2033 import add_2033
from module_2034 import subtract_2034
from module_2035 import multiply_2035
from module_2036 import divide_2036

def test_add_2033():
    assert add_2033(2, 3) == 5

def test_subtract_2034():
    assert subtract_2034(10, 4) == 6

def test_multiply_2035():
    assert multiply_2035(3, 7) == 21

def test_divide_2036():
    assert divide_2036(10, 2) == 5.0
