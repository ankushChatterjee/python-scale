"""Tests for test module 1125 — covers src modules [4497, 4498, 4499, 4500]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4497 import add_4497
from module_4498 import subtract_4498
from module_4499 import multiply_4499
from module_4500 import divide_4500

def test_add_4497():
    assert add_4497(2, 3) == 5

def test_subtract_4498():
    assert subtract_4498(10, 4) == 6

def test_multiply_4499():
    assert multiply_4499(3, 7) == 21

def test_divide_4500():
    assert divide_4500(10, 2) == 5.0
