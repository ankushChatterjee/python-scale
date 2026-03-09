"""Tests for test module 2227 — covers src modules [8905, 8906, 8907, 8908]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8905 import add_8905
from module_8906 import subtract_8906
from module_8907 import multiply_8907
from module_8908 import divide_8908

def test_add_8905():
    assert add_8905(2, 3) == 5

def test_subtract_8906():
    assert subtract_8906(10, 4) == 6

def test_multiply_8907():
    assert multiply_8907(3, 7) == 21

def test_divide_8908():
    assert divide_8908(10, 2) == 5.0
