"""Tests for test module 875 — covers src modules [3497, 3498, 3499, 3500]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3497 import add_3497
from module_3498 import subtract_3498
from module_3499 import multiply_3499
from module_3500 import divide_3500

def test_add_3497():
    assert add_3497(2, 3) == 5

def test_subtract_3498():
    assert subtract_3498(10, 4) == 6

def test_multiply_3499():
    assert multiply_3499(3, 7) == 21

def test_divide_3500():
    assert divide_3500(10, 2) == 5.0
