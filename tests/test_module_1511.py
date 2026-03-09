"""Tests for test module 1511 — covers src modules [6041, 6042, 6043, 6044]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6041 import add_6041
from module_6042 import subtract_6042
from module_6043 import multiply_6043
from module_6044 import divide_6044

def test_add_6041():
    assert add_6041(2, 3) == 5

def test_subtract_6042():
    assert subtract_6042(10, 4) == 6

def test_multiply_6043():
    assert multiply_6043(3, 7) == 21

def test_divide_6044():
    assert divide_6044(10, 2) == 5.0
