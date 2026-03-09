"""Tests for test module 1477 — covers src modules [5905, 5906, 5907, 5908]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5905 import add_5905
from module_5906 import subtract_5906
from module_5907 import multiply_5907
from module_5908 import divide_5908

def test_add_5905():
    assert add_5905(2, 3) == 5

def test_subtract_5906():
    assert subtract_5906(10, 4) == 6

def test_multiply_5907():
    assert multiply_5907(3, 7) == 21

def test_divide_5908():
    assert divide_5908(10, 2) == 5.0
