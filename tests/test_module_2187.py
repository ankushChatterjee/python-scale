"""Tests for test module 2187 — covers src modules [8745, 8746, 8747, 8748]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8745 import add_8745
from module_8746 import subtract_8746
from module_8747 import multiply_8747
from module_8748 import divide_8748

def test_add_8745():
    assert add_8745(2, 3) == 5

def test_subtract_8746():
    assert subtract_8746(10, 4) == 6

def test_multiply_8747():
    assert multiply_8747(3, 7) == 21

def test_divide_8748():
    assert divide_8748(10, 2) == 5.0
