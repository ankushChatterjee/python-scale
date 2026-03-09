"""Tests for test module 1085 — covers src modules [4337, 4338, 4339, 4340]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4337 import add_4337
from module_4338 import subtract_4338
from module_4339 import multiply_4339
from module_4340 import divide_4340

def test_add_4337():
    assert add_4337(2, 3) == 5

def test_subtract_4338():
    assert subtract_4338(10, 4) == 6

def test_multiply_4339():
    assert multiply_4339(3, 7) == 21

def test_divide_4340():
    assert divide_4340(10, 2) == 5.0
