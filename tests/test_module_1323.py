"""Tests for test module 1323 — covers src modules [5289, 5290, 5291, 5292]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5289 import add_5289
from module_5290 import subtract_5290
from module_5291 import multiply_5291
from module_5292 import divide_5292

def test_add_5289():
    assert add_5289(2, 3) == 5

def test_subtract_5290():
    assert subtract_5290(10, 4) == 6

def test_multiply_5291():
    assert multiply_5291(3, 7) == 21

def test_divide_5292():
    assert divide_5292(10, 2) == 5.0
