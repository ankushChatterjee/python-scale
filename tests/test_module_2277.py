"""Tests for test module 2277 — covers src modules [9105, 9106, 9107, 9108]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9105 import add_9105
from module_9106 import subtract_9106
from module_9107 import multiply_9107
from module_9108 import divide_9108

def test_add_9105():
    assert add_9105(2, 3) == 5

def test_subtract_9106():
    assert subtract_9106(10, 4) == 6

def test_multiply_9107():
    assert multiply_9107(3, 7) == 21

def test_divide_9108():
    assert divide_9108(10, 2) == 5.0
