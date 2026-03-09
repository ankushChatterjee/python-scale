"""Tests for test module 1335 — covers src modules [5337, 5338, 5339, 5340]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5337 import add_5337
from module_5338 import subtract_5338
from module_5339 import multiply_5339
from module_5340 import divide_5340

def test_add_5337():
    assert add_5337(2, 3) == 5

def test_subtract_5338():
    assert subtract_5338(10, 4) == 6

def test_multiply_5339():
    assert multiply_5339(3, 7) == 21

def test_divide_5340():
    assert divide_5340(10, 2) == 5.0
