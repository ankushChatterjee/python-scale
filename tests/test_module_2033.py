"""Tests for test module 2033 — covers src modules [8129, 8130, 8131, 8132]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8129 import add_8129
from module_8130 import subtract_8130
from module_8131 import multiply_8131
from module_8132 import divide_8132

def test_add_8129():
    assert add_8129(2, 3) == 5

def test_subtract_8130():
    assert subtract_8130(10, 4) == 6

def test_multiply_8131():
    assert multiply_8131(3, 7) == 21

def test_divide_8132():
    assert divide_8132(10, 2) == 5.0
