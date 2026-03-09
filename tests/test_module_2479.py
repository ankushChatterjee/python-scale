"""Tests for test module 2479 — covers src modules [9913, 9914, 9915, 9916]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9913 import add_9913
from module_9914 import subtract_9914
from module_9915 import multiply_9915
from module_9916 import divide_9916

def test_add_9913():
    assert add_9913(2, 3) == 5

def test_subtract_9914():
    assert subtract_9914(10, 4) == 6

def test_multiply_9915():
    assert multiply_9915(3, 7) == 21

def test_divide_9916():
    assert divide_9916(10, 2) == 5.0
