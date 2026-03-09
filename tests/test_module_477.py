"""Tests for test module 477 — covers src modules [1905, 1906, 1907, 1908]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1905 import add_1905
from module_1906 import subtract_1906
from module_1907 import multiply_1907
from module_1908 import divide_1908

def test_add_1905():
    assert add_1905(2, 3) == 5

def test_subtract_1906():
    assert subtract_1906(10, 4) == 6

def test_multiply_1907():
    assert multiply_1907(3, 7) == 21

def test_divide_1908():
    assert divide_1908(10, 2) == 5.0
