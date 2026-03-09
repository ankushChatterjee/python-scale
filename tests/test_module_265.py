"""Tests for test module 265 — covers src modules [1057, 1058, 1059, 1060]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1057 import add_1057
from module_1058 import subtract_1058
from module_1059 import multiply_1059
from module_1060 import divide_1060

def test_add_1057():
    assert add_1057(2, 3) == 5

def test_subtract_1058():
    assert subtract_1058(10, 4) == 6

def test_multiply_1059():
    assert multiply_1059(3, 7) == 21

def test_divide_1060():
    assert divide_1060(10, 2) == 5.0
