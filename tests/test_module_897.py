"""Tests for test module 897 — covers src modules [3585, 3586, 3587, 3588]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3585 import add_3585
from module_3586 import subtract_3586
from module_3587 import multiply_3587
from module_3588 import divide_3588

def test_add_3585():
    assert add_3585(2, 3) == 5

def test_subtract_3586():
    assert subtract_3586(10, 4) == 6

def test_multiply_3587():
    assert multiply_3587(3, 7) == 21

def test_divide_3588():
    assert divide_3588(10, 2) == 5.0
