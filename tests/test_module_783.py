"""Tests for test module 783 — covers src modules [3129, 3130, 3131, 3132]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3129 import add_3129
from module_3130 import subtract_3130
from module_3131 import multiply_3131
from module_3132 import divide_3132

def test_add_3129():
    assert add_3129(2, 3) == 5

def test_subtract_3130():
    assert subtract_3130(10, 4) == 6

def test_multiply_3131():
    assert multiply_3131(3, 7) == 21

def test_divide_3132():
    assert divide_3132(10, 2) == 5.0
