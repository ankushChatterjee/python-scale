"""Tests for test module 2085 — covers src modules [8337, 8338, 8339, 8340]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8337 import add_8337
from module_8338 import subtract_8338
from module_8339 import multiply_8339
from module_8340 import divide_8340

def test_add_8337():
    assert add_8337(2, 3) == 5

def test_subtract_8338():
    assert subtract_8338(10, 4) == 6

def test_multiply_8339():
    assert multiply_8339(3, 7) == 21

def test_divide_8340():
    assert divide_8340(10, 2) == 5.0
