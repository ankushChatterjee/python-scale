"""Tests for test module 511 — covers src modules [2041, 2042, 2043, 2044]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2041 import add_2041
from module_2042 import subtract_2042
from module_2043 import multiply_2043
from module_2044 import divide_2044

def test_add_2041():
    assert add_2041(2, 3) == 5

def test_subtract_2042():
    assert subtract_2042(10, 4) == 6

def test_multiply_2043():
    assert multiply_2043(3, 7) == 21

def test_divide_2044():
    assert divide_2044(10, 2) == 5.0
