"""Tests for test module 1585 — covers src modules [6337, 6338, 6339, 6340]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6337 import add_6337
from module_6338 import subtract_6338
from module_6339 import multiply_6339
from module_6340 import divide_6340

def test_add_6337():
    assert add_6337(2, 3) == 5

def test_subtract_6338():
    assert subtract_6338(10, 4) == 6

def test_multiply_6339():
    assert multiply_6339(3, 7) == 21

def test_divide_6340():
    assert divide_6340(10, 2) == 5.0
