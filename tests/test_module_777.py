"""Tests for test module 777 — covers src modules [3105, 3106, 3107, 3108]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3105 import add_3105
from module_3106 import subtract_3106
from module_3107 import multiply_3107
from module_3108 import divide_3108

def test_add_3105():
    assert add_3105(2, 3) == 5

def test_subtract_3106():
    assert subtract_3106(10, 4) == 6

def test_multiply_3107():
    assert multiply_3107(3, 7) == 21

def test_divide_3108():
    assert divide_3108(10, 2) == 5.0
