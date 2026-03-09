"""Tests for test module 1971 — covers src modules [7881, 7882, 7883, 7884]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7881 import add_7881
from module_7882 import subtract_7882
from module_7883 import multiply_7883
from module_7884 import divide_7884

def test_add_7881():
    assert add_7881(2, 3) == 5

def test_subtract_7882():
    assert subtract_7882(10, 4) == 6

def test_multiply_7883():
    assert multiply_7883(3, 7) == 21

def test_divide_7884():
    assert divide_7884(10, 2) == 5.0
