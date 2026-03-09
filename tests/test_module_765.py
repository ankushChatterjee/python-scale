"""Tests for test module 765 — covers src modules [3057, 3058, 3059, 3060]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3057 import add_3057
from module_3058 import subtract_3058
from module_3059 import multiply_3059
from module_3060 import divide_3060

def test_add_3057():
    assert add_3057(2, 3) == 5

def test_subtract_3058():
    assert subtract_3058(10, 4) == 6

def test_multiply_3059():
    assert multiply_3059(3, 7) == 21

def test_divide_3060():
    assert divide_3060(10, 2) == 5.0
