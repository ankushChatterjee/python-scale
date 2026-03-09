"""Tests for test module 823 — covers src modules [3289, 3290, 3291, 3292]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3289 import add_3289
from module_3290 import subtract_3290
from module_3291 import multiply_3291
from module_3292 import divide_3292

def test_add_3289():
    assert add_3289(2, 3) == 5

def test_subtract_3290():
    assert subtract_3290(10, 4) == 6

def test_multiply_3291():
    assert multiply_3291(3, 7) == 21

def test_divide_3292():
    assert divide_3292(10, 2) == 5.0
