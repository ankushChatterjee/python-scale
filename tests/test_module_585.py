"""Tests for test module 585 — covers src modules [2337, 2338, 2339, 2340]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2337 import add_2337
from module_2338 import subtract_2338
from module_2339 import multiply_2339
from module_2340 import divide_2340

def test_add_2337():
    assert add_2337(2, 3) == 5

def test_subtract_2338():
    assert subtract_2338(10, 4) == 6

def test_multiply_2339():
    assert multiply_2339(3, 7) == 21

def test_divide_2340():
    assert divide_2340(10, 2) == 5.0
