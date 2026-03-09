"""Tests for test module 471 — covers src modules [1881, 1882, 1883, 1884]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1881 import add_1881
from module_1882 import subtract_1882
from module_1883 import multiply_1883
from module_1884 import divide_1884

def test_add_1881():
    assert add_1881(2, 3) == 5

def test_subtract_1882():
    assert subtract_1882(10, 4) == 6

def test_multiply_1883():
    assert multiply_1883(3, 7) == 21

def test_divide_1884():
    assert divide_1884(10, 2) == 5.0
