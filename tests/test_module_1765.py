"""Tests for test module 1765 — covers src modules [7057, 7058, 7059, 7060]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7057 import add_7057
from module_7058 import subtract_7058
from module_7059 import multiply_7059
from module_7060 import divide_7060

def test_add_7057():
    assert add_7057(2, 3) == 5

def test_subtract_7058():
    assert subtract_7058(10, 4) == 6

def test_multiply_7059():
    assert multiply_7059(3, 7) == 21

def test_divide_7060():
    assert divide_7060(10, 2) == 5.0
