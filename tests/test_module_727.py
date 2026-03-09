"""Tests for test module 727 — covers src modules [2905, 2906, 2907, 2908]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2905 import add_2905
from module_2906 import subtract_2906
from module_2907 import multiply_2907
from module_2908 import divide_2908

def test_add_2905():
    assert add_2905(2, 3) == 5

def test_subtract_2906():
    assert subtract_2906(10, 4) == 6

def test_multiply_2907():
    assert multiply_2907(3, 7) == 21

def test_divide_2908():
    assert divide_2908(10, 2) == 5.0
