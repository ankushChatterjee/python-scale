"""Tests for test module 1229 — covers src modules [4913, 4914, 4915, 4916]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4913 import add_4913
from module_4914 import subtract_4914
from module_4915 import multiply_4915
from module_4916 import divide_4916

def test_add_4913():
    assert add_4913(2, 3) == 5

def test_subtract_4914():
    assert subtract_4914(10, 4) == 6

def test_multiply_4915():
    assert multiply_4915(3, 7) == 21

def test_divide_4916():
    assert divide_4916(10, 2) == 5.0
