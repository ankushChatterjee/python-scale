"""Tests for test module 73 — covers src modules [289, 290, 291, 292]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_289 import add_289
from module_290 import subtract_290
from module_291 import multiply_291
from module_292 import divide_292

def test_add_289():
    assert add_289(2, 3) == 5

def test_subtract_290():
    assert subtract_290(10, 4) == 6

def test_multiply_291():
    assert multiply_291(3, 7) == 21

def test_divide_292():
    assert divide_292(10, 2) == 5.0
