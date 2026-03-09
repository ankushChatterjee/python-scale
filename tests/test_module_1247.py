"""Tests for test module 1247 — covers src modules [4985, 4986, 4987, 4988]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4985 import add_4985
from module_4986 import subtract_4986
from module_4987 import multiply_4987
from module_4988 import divide_4988

def test_add_4985():
    assert add_4985(2, 3) == 5

def test_subtract_4986():
    assert subtract_4986(10, 4) == 6

def test_multiply_4987():
    assert multiply_4987(3, 7) == 21

def test_divide_4988():
    assert divide_4988(10, 2) == 5.0
