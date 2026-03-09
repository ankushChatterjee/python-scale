"""Tests for test module 293 — covers src modules [1169, 1170, 1171, 1172]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1169 import add_1169
from module_1170 import subtract_1170
from module_1171 import multiply_1171
from module_1172 import divide_1172

def test_add_1169():
    assert add_1169(2, 3) == 5

def test_subtract_1170():
    assert subtract_1170(10, 4) == 6

def test_multiply_1171():
    assert multiply_1171(3, 7) == 21

def test_divide_1172():
    assert divide_1172(10, 2) == 5.0
