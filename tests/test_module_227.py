"""Tests for test module 227 — covers src modules [905, 906, 907, 908]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_905 import add_905
from module_906 import subtract_906
from module_907 import multiply_907
from module_908 import divide_908

def test_add_905():
    assert add_905(2, 3) == 5

def test_subtract_906():
    assert subtract_906(10, 4) == 6

def test_multiply_907():
    assert multiply_907(3, 7) == 21

def test_divide_908():
    assert divide_908(10, 2) == 5.0
