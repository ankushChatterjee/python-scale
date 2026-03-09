"""Tests for test module 1721 — covers src modules [6881, 6882, 6883, 6884]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6881 import add_6881
from module_6882 import subtract_6882
from module_6883 import multiply_6883
from module_6884 import divide_6884

def test_add_6881():
    assert add_6881(2, 3) == 5

def test_subtract_6882():
    assert subtract_6882(10, 4) == 6

def test_multiply_6883():
    assert multiply_6883(3, 7) == 21

def test_divide_6884():
    assert divide_6884(10, 2) == 5.0
