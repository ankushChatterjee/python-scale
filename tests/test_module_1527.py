"""Tests for test module 1527 — covers src modules [6105, 6106, 6107, 6108]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6105 import add_6105
from module_6106 import subtract_6106
from module_6107 import multiply_6107
from module_6108 import divide_6108

def test_add_6105():
    assert add_6105(2, 3) == 5

def test_subtract_6106():
    assert subtract_6106(10, 4) == 6

def test_multiply_6107():
    assert multiply_6107(3, 7) == 21

def test_divide_6108():
    assert divide_6108(10, 2) == 5.0
