"""Tests for test module 259 — covers src modules [1033, 1034, 1035, 1036]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1033 import add_1033
from module_1034 import subtract_1034
from module_1035 import multiply_1035
from module_1036 import divide_1036

def test_add_1033():
    assert add_1033(2, 3) == 5

def test_subtract_1034():
    assert subtract_1034(10, 4) == 6

def test_multiply_1035():
    assert multiply_1035(3, 7) == 21

def test_divide_1036():
    assert divide_1036(10, 2) == 5.0
