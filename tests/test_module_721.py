"""Tests for test module 721 — covers src modules [2881, 2882, 2883, 2884]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2881 import add_2881
from module_2882 import subtract_2882
from module_2883 import multiply_2883
from module_2884 import divide_2884

def test_add_2881():
    assert add_2881(2, 3) == 5

def test_subtract_2882():
    assert subtract_2882(10, 4) == 6

def test_multiply_2883():
    assert multiply_2883(3, 7) == 21

def test_divide_2884():
    assert divide_2884(10, 2) == 5.0
