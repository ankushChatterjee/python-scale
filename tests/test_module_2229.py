"""Tests for test module 2229 — covers src modules [8913, 8914, 8915, 8916]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8913 import add_8913
from module_8914 import subtract_8914
from module_8915 import multiply_8915
from module_8916 import divide_8916

def test_add_8913():
    assert add_8913(2, 3) == 5

def test_subtract_8914():
    assert subtract_8914(10, 4) == 6

def test_multiply_8915():
    assert multiply_8915(3, 7) == 21

def test_divide_8916():
    assert divide_8916(10, 2) == 5.0
