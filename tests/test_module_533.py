"""Tests for test module 533 — covers src modules [2129, 2130, 2131, 2132]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2129 import add_2129
from module_2130 import subtract_2130
from module_2131 import multiply_2131
from module_2132 import divide_2132

def test_add_2129():
    assert add_2129(2, 3) == 5

def test_subtract_2130():
    assert subtract_2130(10, 4) == 6

def test_multiply_2131():
    assert multiply_2131(3, 7) == 21

def test_divide_2132():
    assert divide_2132(10, 2) == 5.0
