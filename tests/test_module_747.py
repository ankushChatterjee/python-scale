"""Tests for test module 747 — covers src modules [2985, 2986, 2987, 2988]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2985 import add_2985
from module_2986 import subtract_2986
from module_2987 import multiply_2987
from module_2988 import divide_2988

def test_add_2985():
    assert add_2985(2, 3) == 5

def test_subtract_2986():
    assert subtract_2986(10, 4) == 6

def test_multiply_2987():
    assert multiply_2987(3, 7) == 21

def test_divide_2988():
    assert divide_2988(10, 2) == 5.0
