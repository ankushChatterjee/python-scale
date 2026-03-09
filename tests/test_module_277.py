"""Tests for test module 277 — covers src modules [1105, 1106, 1107, 1108]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1105 import add_1105
from module_1106 import subtract_1106
from module_1107 import multiply_1107
from module_1108 import divide_1108

def test_add_1105():
    assert add_1105(2, 3) == 5

def test_subtract_1106():
    assert subtract_1106(10, 4) == 6

def test_multiply_1107():
    assert multiply_1107(3, 7) == 21

def test_divide_1108():
    assert divide_1108(10, 2) == 5.0
