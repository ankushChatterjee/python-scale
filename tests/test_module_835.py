"""Tests for test module 835 — covers src modules [3337, 3338, 3339, 3340]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3337 import add_3337
from module_3338 import subtract_3338
from module_3339 import multiply_3339
from module_3340 import divide_3340

def test_add_3337():
    assert add_3337(2, 3) == 5

def test_subtract_3338():
    assert subtract_3338(10, 4) == 6

def test_multiply_3339():
    assert multiply_3339(3, 7) == 21

def test_divide_3340():
    assert divide_3340(10, 2) == 5.0
