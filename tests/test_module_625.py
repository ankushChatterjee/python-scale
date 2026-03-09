"""Tests for test module 625 — covers src modules [2497, 2498, 2499, 2500]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2497 import add_2497
from module_2498 import subtract_2498
from module_2499 import multiply_2499
from module_2500 import divide_2500

def test_add_2497():
    assert add_2497(2, 3) == 5

def test_subtract_2498():
    assert subtract_2498(10, 4) == 6

def test_multiply_2499():
    assert multiply_2499(3, 7) == 21

def test_divide_2500():
    assert divide_2500(10, 2) == 5.0
