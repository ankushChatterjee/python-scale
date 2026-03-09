"""Tests for test module 497 — covers src modules [1985, 1986, 1987, 1988]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1985 import add_1985
from module_1986 import subtract_1986
from module_1987 import multiply_1987
from module_1988 import divide_1988

def test_add_1985():
    assert add_1985(2, 3) == 5

def test_subtract_1986():
    assert subtract_1986(10, 4) == 6

def test_multiply_1987():
    assert multiply_1987(3, 7) == 21

def test_divide_1988():
    assert divide_1988(10, 2) == 5.0
