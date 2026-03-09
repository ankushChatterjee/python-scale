"""Tests for test module 1777 — covers src modules [7105, 7106, 7107, 7108]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7105 import add_7105
from module_7106 import subtract_7106
from module_7107 import multiply_7107
from module_7108 import divide_7108

def test_add_7105():
    assert add_7105(2, 3) == 5

def test_subtract_7106():
    assert subtract_7106(10, 4) == 6

def test_multiply_7107():
    assert multiply_7107(3, 7) == 21

def test_divide_7108():
    assert divide_7108(10, 2) == 5.0
