"""Tests for test module 1761 — covers src modules [7041, 7042, 7043, 7044]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7041 import add_7041
from module_7042 import subtract_7042
from module_7043 import multiply_7043
from module_7044 import divide_7044

def test_add_7041():
    assert add_7041(2, 3) == 5

def test_subtract_7042():
    assert subtract_7042(10, 4) == 6

def test_multiply_7043():
    assert multiply_7043(3, 7) == 21

def test_divide_7044():
    assert divide_7044(10, 2) == 5.0
