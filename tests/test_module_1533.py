"""Tests for test module 1533 — covers src modules [6129, 6130, 6131, 6132]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6129 import add_6129
from module_6130 import subtract_6130
from module_6131 import multiply_6131
from module_6132 import divide_6132

def test_add_6129():
    assert add_6129(2, 3) == 5

def test_subtract_6130():
    assert subtract_6130(10, 4) == 6

def test_multiply_6131():
    assert multiply_6131(3, 7) == 21

def test_divide_6132():
    assert divide_6132(10, 2) == 5.0
