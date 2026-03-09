"""Tests for test module 1835 — covers src modules [7337, 7338, 7339, 7340]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7337 import add_7337
from module_7338 import subtract_7338
from module_7339 import multiply_7339
from module_7340 import divide_7340

def test_add_7337():
    assert add_7337(2, 3) == 5

def test_subtract_7338():
    assert subtract_7338(10, 4) == 6

def test_multiply_7339():
    assert multiply_7339(3, 7) == 21

def test_divide_7340():
    assert divide_7340(10, 2) == 5.0
