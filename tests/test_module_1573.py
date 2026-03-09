"""Tests for test module 1573 — covers src modules [6289, 6290, 6291, 6292]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6289 import add_6289
from module_6290 import subtract_6290
from module_6291 import multiply_6291
from module_6292 import divide_6292

def test_add_6289():
    assert add_6289(2, 3) == 5

def test_subtract_6290():
    assert subtract_6290(10, 4) == 6

def test_multiply_6291():
    assert multiply_6291(3, 7) == 21

def test_divide_6292():
    assert divide_6292(10, 2) == 5.0
