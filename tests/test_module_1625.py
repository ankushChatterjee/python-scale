"""Tests for test module 1625 — covers src modules [6497, 6498, 6499, 6500]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6497 import add_6497
from module_6498 import subtract_6498
from module_6499 import multiply_6499
from module_6500 import divide_6500

def test_add_6497():
    assert add_6497(2, 3) == 5

def test_subtract_6498():
    assert subtract_6498(10, 4) == 6

def test_multiply_6499():
    assert multiply_6499(3, 7) == 21

def test_divide_6500():
    assert divide_6500(10, 2) == 5.0
