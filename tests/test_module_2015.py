"""Tests for test module 2015 — covers src modules [8057, 8058, 8059, 8060]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8057 import add_8057
from module_8058 import subtract_8058
from module_8059 import multiply_8059
from module_8060 import divide_8060

def test_add_8057():
    assert add_8057(2, 3) == 5

def test_subtract_8058():
    assert subtract_8058(10, 4) == 6

def test_multiply_8059():
    assert multiply_8059(3, 7) == 21

def test_divide_8060():
    assert divide_8060(10, 2) == 5.0
