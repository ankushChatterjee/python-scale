"""Tests for test module 283 — covers src modules [1129, 1130, 1131, 1132]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1129 import add_1129
from module_1130 import subtract_1130
from module_1131 import multiply_1131
from module_1132 import divide_1132

def test_add_1129():
    assert add_1129(2, 3) == 5

def test_subtract_1130():
    assert subtract_1130(10, 4) == 6

def test_multiply_1131():
    assert multiply_1131(3, 7) == 21

def test_divide_1132():
    assert divide_1132(10, 2) == 5.0
