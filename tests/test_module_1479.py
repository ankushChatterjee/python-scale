"""Tests for test module 1479 — covers src modules [5913, 5914, 5915, 5916]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5913 import add_5913
from module_5914 import subtract_5914
from module_5915 import multiply_5915
from module_5916 import divide_5916

def test_add_5913():
    assert add_5913(2, 3) == 5

def test_subtract_5914():
    assert subtract_5914(10, 4) == 6

def test_multiply_5915():
    assert multiply_5915(3, 7) == 21

def test_divide_5916():
    assert divide_5916(10, 2) == 5.0
