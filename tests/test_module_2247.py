"""Tests for test module 2247 — covers src modules [8985, 8986, 8987, 8988]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8985 import add_8985
from module_8986 import subtract_8986
from module_8987 import multiply_8987
from module_8988 import divide_8988

def test_add_8985():
    assert add_8985(2, 3) == 5

def test_subtract_8986():
    assert subtract_8986(10, 4) == 6

def test_multiply_8987():
    assert multiply_8987(3, 7) == 21

def test_divide_8988():
    assert divide_8988(10, 2) == 5.0
