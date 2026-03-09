"""Tests for test module 1977 — covers src modules [7905, 7906, 7907, 7908]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7905 import add_7905
from module_7906 import subtract_7906
from module_7907 import multiply_7907
from module_7908 import divide_7908

def test_add_7905():
    assert add_7905(2, 3) == 5

def test_subtract_7906():
    assert subtract_7906(10, 4) == 6

def test_multiply_7907():
    assert multiply_7907(3, 7) == 21

def test_divide_7908():
    assert divide_7908(10, 2) == 5.0
