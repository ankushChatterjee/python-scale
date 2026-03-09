"""Tests for test module 1283 — covers src modules [5129, 5130, 5131, 5132]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5129 import add_5129
from module_5130 import subtract_5130
from module_5131 import multiply_5131
from module_5132 import divide_5132

def test_add_5129():
    assert add_5129(2, 3) == 5

def test_subtract_5130():
    assert subtract_5130(10, 4) == 6

def test_multiply_5131():
    assert multiply_5131(3, 7) == 21

def test_divide_5132():
    assert divide_5132(10, 2) == 5.0
