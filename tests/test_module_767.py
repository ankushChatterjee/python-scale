"""Tests for test module 767 — covers src modules [3065, 3066, 3067, 3068]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3065 import add_3065
from module_3066 import subtract_3066
from module_3067 import multiply_3067
from module_3068 import divide_3068

def test_add_3065():
    assert add_3065(2, 3) == 5

def test_subtract_3066():
    assert subtract_3066(10, 4) == 6

def test_multiply_3067():
    assert multiply_3067(3, 7) == 21

def test_divide_3068():
    assert divide_3068(10, 2) == 5.0
