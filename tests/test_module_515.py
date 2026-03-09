"""Tests for test module 515 — covers src modules [2057, 2058, 2059, 2060]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2057 import add_2057
from module_2058 import subtract_2058
from module_2059 import multiply_2059
from module_2060 import divide_2060

def test_add_2057():
    assert add_2057(2, 3) == 5

def test_subtract_2058():
    assert subtract_2058(10, 4) == 6

def test_multiply_2059():
    assert multiply_2059(3, 7) == 21

def test_divide_2060():
    assert divide_2060(10, 2) == 5.0
