"""Tests for test module 1033 — covers src modules [4129, 4130, 4131, 4132]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4129 import add_4129
from module_4130 import subtract_4130
from module_4131 import multiply_4131
from module_4132 import divide_4132

def test_add_4129():
    assert add_4129(2, 3) == 5

def test_subtract_4130():
    assert subtract_4130(10, 4) == 6

def test_multiply_4131():
    assert multiply_4131(3, 7) == 21

def test_divide_4132():
    assert divide_4132(10, 2) == 5.0
