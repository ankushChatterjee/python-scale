"""Tests for test module 997 — covers src modules [3985, 3986, 3987, 3988]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3985 import add_3985
from module_3986 import subtract_3986
from module_3987 import multiply_3987
from module_3988 import divide_3988

def test_add_3985():
    assert add_3985(2, 3) == 5

def test_subtract_3986():
    assert subtract_3986(10, 4) == 6

def test_multiply_3987():
    assert multiply_3987(3, 7) == 21

def test_divide_3988():
    assert divide_3988(10, 2) == 5.0
