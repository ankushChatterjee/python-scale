"""Tests for test module 247 — covers src modules [985, 986, 987, 988]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_985 import add_985
from module_986 import subtract_986
from module_987 import multiply_987
from module_988 import divide_988

def test_add_985():
    assert add_985(2, 3) == 5

def test_subtract_986():
    assert subtract_986(10, 4) == 6

def test_multiply_987():
    assert multiply_987(3, 7) == 21

def test_divide_988():
    assert divide_988(10, 2) == 5.0
