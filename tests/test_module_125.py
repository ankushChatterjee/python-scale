"""Tests for test module 125 — covers src modules [497, 498, 499, 500]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_497 import add_497
from module_498 import subtract_498
from module_499 import multiply_499
from module_500 import divide_500

def test_add_497():
    assert add_497(2, 3) == 5

def test_subtract_498():
    assert subtract_498(10, 4) == 6

def test_multiply_499():
    assert multiply_499(3, 7) == 21

def test_divide_500():
    assert divide_500(10, 2) == 5.0
