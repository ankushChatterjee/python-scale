"""Tests for test module 33 — covers src modules [129, 130, 131, 132]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_129 import add_129
from module_130 import subtract_130
from module_131 import multiply_131
from module_132 import divide_132

def test_add_129():
    assert add_129(2, 3) == 5

def test_subtract_130():
    assert subtract_130(10, 4) == 6

def test_multiply_131():
    assert multiply_131(3, 7) == 21

def test_divide_132():
    assert divide_132(10, 2) == 5.0
