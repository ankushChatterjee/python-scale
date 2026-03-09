"""Tests for test module 1823 — covers src modules [7289, 7290, 7291, 7292]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7289 import add_7289
from module_7290 import subtract_7290
from module_7291 import multiply_7291
from module_7292 import divide_7292

def test_add_7289():
    assert add_7289(2, 3) == 5

def test_subtract_7290():
    assert subtract_7290(10, 4) == 6

def test_multiply_7291():
    assert multiply_7291(3, 7) == 21

def test_divide_7292():
    assert divide_7292(10, 2) == 5.0
