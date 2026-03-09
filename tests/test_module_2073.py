"""Tests for test module 2073 — covers src modules [8289, 8290, 8291, 8292]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8289 import add_8289
from module_8290 import subtract_8290
from module_8291 import multiply_8291
from module_8292 import divide_8292

def test_add_8289():
    assert add_8289(2, 3) == 5

def test_subtract_8290():
    assert subtract_8290(10, 4) == 6

def test_multiply_8291():
    assert multiply_8291(3, 7) == 21

def test_divide_8292():
    assert divide_8292(10, 2) == 5.0
