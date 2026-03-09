"""Tests for test module 1193 — covers src modules [4769, 4770, 4771, 4772]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4769 import add_4769
from module_4770 import subtract_4770
from module_4771 import multiply_4771
from module_4772 import divide_4772

def test_add_4769():
    assert add_4769(2, 3) == 5

def test_subtract_4770():
    assert subtract_4770(10, 4) == 6

def test_multiply_4771():
    assert multiply_4771(3, 7) == 21

def test_divide_4772():
    assert divide_4772(10, 2) == 5.0
