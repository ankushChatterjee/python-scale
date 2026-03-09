"""Tests for test module 1937 — covers src modules [7745, 7746, 7747, 7748]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7745 import add_7745
from module_7746 import subtract_7746
from module_7747 import multiply_7747
from module_7748 import divide_7748

def test_add_7745():
    assert add_7745(2, 3) == 5

def test_subtract_7746():
    assert subtract_7746(10, 4) == 6

def test_multiply_7747():
    assert multiply_7747(3, 7) == 21

def test_divide_7748():
    assert divide_7748(10, 2) == 5.0
