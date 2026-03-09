"""Tests for test module 1747 — covers src modules [6985, 6986, 6987, 6988]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6985 import add_6985
from module_6986 import subtract_6986
from module_6987 import multiply_6987
from module_6988 import divide_6988

def test_add_6985():
    assert add_6985(2, 3) == 5

def test_subtract_6986():
    assert subtract_6986(10, 4) == 6

def test_multiply_6987():
    assert multiply_6987(3, 7) == 21

def test_divide_6988():
    assert divide_6988(10, 2) == 5.0
