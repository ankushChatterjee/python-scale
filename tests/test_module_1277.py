"""Tests for test module 1277 — covers src modules [5105, 5106, 5107, 5108]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5105 import add_5105
from module_5106 import subtract_5106
from module_5107 import multiply_5107
from module_5108 import divide_5108

def test_add_5105():
    assert add_5105(2, 3) == 5

def test_subtract_5106():
    assert subtract_5106(10, 4) == 6

def test_multiply_5107():
    assert multiply_5107(3, 7) == 21

def test_divide_5108():
    assert divide_5108(10, 2) == 5.0
