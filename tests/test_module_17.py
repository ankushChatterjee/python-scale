"""Tests for test module 17 — covers src modules [65, 66, 67, 68]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_65 import add_65
from module_66 import subtract_66
from module_67 import multiply_67
from module_68 import divide_68

def test_add_65():
    assert add_65(2, 3) == 5

def test_subtract_66():
    assert subtract_66(10, 4) == 6

def test_multiply_67():
    assert multiply_67(3, 7) == 21

def test_divide_68():
    assert divide_68(10, 2) == 5.0
