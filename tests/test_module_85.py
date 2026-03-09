"""Tests for test module 85 — covers src modules [337, 338, 339, 340]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_337 import add_337
from module_338 import subtract_338
from module_339 import multiply_339
from module_340 import divide_340

def test_add_337():
    assert add_337(2, 3) == 5

def test_subtract_338():
    assert subtract_338(10, 4) == 6

def test_multiply_339():
    assert multiply_339(3, 7) == 21

def test_divide_340():
    assert divide_340(10, 2) == 5.0
