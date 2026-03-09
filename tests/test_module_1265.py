"""Tests for test module 1265 — covers src modules [5057, 5058, 5059, 5060]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5057 import add_5057
from module_5058 import subtract_5058
from module_5059 import multiply_5059
from module_5060 import divide_5060

def test_add_5057():
    assert add_5057(2, 3) == 5

def test_subtract_5058():
    assert subtract_5058(10, 4) == 6

def test_multiply_5059():
    assert multiply_5059(3, 7) == 21

def test_divide_5060():
    assert divide_5060(10, 2) == 5.0
