"""Tests for test module 1043 — covers src modules [4169, 4170, 4171, 4172]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4169 import add_4169
from module_4170 import subtract_4170
from module_4171 import multiply_4171
from module_4172 import divide_4172

def test_add_4169():
    assert add_4169(2, 3) == 5

def test_subtract_4170():
    assert subtract_4170(10, 4) == 6

def test_multiply_4171():
    assert multiply_4171(3, 7) == 21

def test_divide_4172():
    assert divide_4172(10, 2) == 5.0
