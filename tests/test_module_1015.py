"""Tests for test module 1015 — covers src modules [4057, 4058, 4059, 4060]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4057 import add_4057
from module_4058 import subtract_4058
from module_4059 import multiply_4059
from module_4060 import divide_4060

def test_add_4057():
    assert add_4057(2, 3) == 5

def test_subtract_4058():
    assert subtract_4058(10, 4) == 6

def test_multiply_4059():
    assert multiply_4059(3, 7) == 21

def test_divide_4060():
    assert divide_4060(10, 2) == 5.0
