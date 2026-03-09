"""Tests for test module 1729 — covers src modules [6913, 6914, 6915, 6916]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6913 import add_6913
from module_6914 import subtract_6914
from module_6915 import multiply_6915
from module_6916 import divide_6916

def test_add_6913():
    assert add_6913(2, 3) == 5

def test_subtract_6914():
    assert subtract_6914(10, 4) == 6

def test_multiply_6915():
    assert multiply_6915(3, 7) == 21

def test_divide_6916():
    assert divide_6916(10, 2) == 5.0
