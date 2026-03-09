"""Tests for test module 479 — covers src modules [1913, 1914, 1915, 1916]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1913 import add_1913
from module_1914 import subtract_1914
from module_1915 import multiply_1915
from module_1916 import divide_1916

def test_add_1913():
    assert add_1913(2, 3) == 5

def test_subtract_1914():
    assert subtract_1914(10, 4) == 6

def test_multiply_1915():
    assert multiply_1915(3, 7) == 21

def test_divide_1916():
    assert divide_1916(10, 2) == 5.0
