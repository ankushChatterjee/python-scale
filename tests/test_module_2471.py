"""Tests for test module 2471 — covers src modules [9881, 9882, 9883, 9884]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9881 import add_9881
from module_9882 import subtract_9882
from module_9883 import multiply_9883
from module_9884 import divide_9884

def test_add_9881():
    assert add_9881(2, 3) == 5

def test_subtract_9882():
    assert subtract_9882(10, 4) == 6

def test_multiply_9883():
    assert multiply_9883(3, 7) == 21

def test_divide_9884():
    assert divide_9884(10, 2) == 5.0
