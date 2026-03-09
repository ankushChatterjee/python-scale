"""Tests for test module 729 — covers src modules [2913, 2914, 2915, 2916]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2913 import add_2913
from module_2914 import subtract_2914
from module_2915 import multiply_2915
from module_2916 import divide_2916

def test_add_2913():
    assert add_2913(2, 3) == 5

def test_subtract_2914():
    assert subtract_2914(10, 4) == 6

def test_multiply_2915():
    assert multiply_2915(3, 7) == 21

def test_divide_2916():
    assert divide_2916(10, 2) == 5.0
