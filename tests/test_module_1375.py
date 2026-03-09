"""Tests for test module 1375 — covers src modules [5497, 5498, 5499, 5500]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5497 import add_5497
from module_5498 import subtract_5498
from module_5499 import multiply_5499
from module_5500 import divide_5500

def test_add_5497():
    assert add_5497(2, 3) == 5

def test_subtract_5498():
    assert subtract_5498(10, 4) == 6

def test_multiply_5499():
    assert multiply_5499(3, 7) == 21

def test_divide_5500():
    assert divide_5500(10, 2) == 5.0
