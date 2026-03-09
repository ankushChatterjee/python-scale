"""Tests for test module 1497 — covers src modules [5985, 5986, 5987, 5988]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5985 import add_5985
from module_5986 import subtract_5986
from module_5987 import multiply_5987
from module_5988 import divide_5988

def test_add_5985():
    assert add_5985(2, 3) == 5

def test_subtract_5986():
    assert subtract_5986(10, 4) == 6

def test_multiply_5987():
    assert multiply_5987(3, 7) == 21

def test_divide_5988():
    assert divide_5988(10, 2) == 5.0
