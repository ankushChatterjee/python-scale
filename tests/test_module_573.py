"""Tests for test module 573 — covers src modules [2289, 2290, 2291, 2292]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2289 import add_2289
from module_2290 import subtract_2290
from module_2291 import multiply_2291
from module_2292 import divide_2292

def test_add_2289():
    assert add_2289(2, 3) == 5

def test_subtract_2290():
    assert subtract_2290(10, 4) == 6

def test_multiply_2291():
    assert multiply_2291(3, 7) == 21

def test_divide_2292():
    assert divide_2292(10, 2) == 5.0
