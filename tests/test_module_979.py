"""Tests for test module 979 — covers src modules [3913, 3914, 3915, 3916]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3913 import add_3913
from module_3914 import subtract_3914
from module_3915 import multiply_3915
from module_3916 import divide_3916

def test_add_3913():
    assert add_3913(2, 3) == 5

def test_subtract_3914():
    assert subtract_3914(10, 4) == 6

def test_multiply_3915():
    assert multiply_3915(3, 7) == 21

def test_divide_3916():
    assert divide_3916(10, 2) == 5.0
