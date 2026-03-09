"""Tests for test module 761 — covers src modules [3041, 3042, 3043, 3044]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3041 import add_3041
from module_3042 import subtract_3042
from module_3043 import multiply_3043
from module_3044 import divide_3044

def test_add_3041():
    assert add_3041(2, 3) == 5

def test_subtract_3042():
    assert subtract_3042(10, 4) == 6

def test_multiply_3043():
    assert multiply_3043(3, 7) == 21

def test_divide_3044():
    assert divide_3044(10, 2) == 5.0
