"""Tests for test module 1073 — covers src modules [4289, 4290, 4291, 4292]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4289 import add_4289
from module_4290 import subtract_4290
from module_4291 import multiply_4291
from module_4292 import divide_4292

def test_add_4289():
    assert add_4289(2, 3) == 5

def test_subtract_4290():
    assert subtract_4290(10, 4) == 6

def test_multiply_4291():
    assert multiply_4291(3, 7) == 21

def test_divide_4292():
    assert divide_4292(10, 2) == 5.0
