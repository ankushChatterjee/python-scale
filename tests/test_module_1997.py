"""Tests for test module 1997 — covers src modules [7985, 7986, 7987, 7988]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7985 import add_7985
from module_7986 import subtract_7986
from module_7987 import multiply_7987
from module_7988 import divide_7988

def test_add_7985():
    assert add_7985(2, 3) == 5

def test_subtract_7986():
    assert subtract_7986(10, 4) == 6

def test_multiply_7987():
    assert multiply_7987(3, 7) == 21

def test_divide_7988():
    assert divide_7988(10, 2) == 5.0
