"""Tests for test module 5 — covers src modules [17, 18, 19, 20]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_17 import add_17
from module_18 import subtract_18
from module_19 import multiply_19
from module_20 import divide_20

def test_add_17():
    assert add_17(2, 3) == 5

def test_subtract_18():
    assert subtract_18(10, 4) == 6

def test_multiply_19():
    assert multiply_19(3, 7) == 21

def test_divide_20():
    assert divide_20(10, 2) == 5.0
