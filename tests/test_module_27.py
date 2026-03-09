"""Tests for test module 27 — covers src modules [105, 106, 107, 108]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_105 import add_105
from module_106 import subtract_106
from module_107 import multiply_107
from module_108 import divide_108

def test_add_105():
    assert add_105(2, 3) == 5

def test_subtract_106():
    assert subtract_106(10, 4) == 6

def test_multiply_107():
    assert multiply_107(3, 7) == 21

def test_divide_108():
    assert divide_108(10, 2) == 5.0
