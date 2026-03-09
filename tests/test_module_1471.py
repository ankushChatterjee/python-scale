"""Tests for test module 1471 — covers src modules [5881, 5882, 5883, 5884]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5881 import add_5881
from module_5882 import subtract_5882
from module_5883 import multiply_5883
from module_5884 import divide_5884

def test_add_5881():
    assert add_5881(2, 3) == 5

def test_subtract_5882():
    assert subtract_5882(10, 4) == 6

def test_multiply_5883():
    assert multiply_5883(3, 7) == 21

def test_divide_5884():
    assert divide_5884(10, 2) == 5.0
