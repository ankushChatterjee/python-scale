"""Tests for test module 1979 — covers src modules [7913, 7914, 7915, 7916]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7913 import add_7913
from module_7914 import subtract_7914
from module_7915 import multiply_7915
from module_7916 import divide_7916

def test_add_7913():
    assert add_7913(2, 3) == 5

def test_subtract_7914():
    assert subtract_7914(10, 4) == 6

def test_multiply_7915():
    assert multiply_7915(3, 7) == 21

def test_divide_7916():
    assert divide_7916(10, 2) == 5.0
