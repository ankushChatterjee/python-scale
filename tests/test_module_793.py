"""Tests for test module 793 — covers src modules [3169, 3170, 3171, 3172]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3169 import add_3169
from module_3170 import subtract_3170
from module_3171 import multiply_3171
from module_3172 import divide_3172

def test_add_3169():
    assert add_3169(2, 3) == 5

def test_subtract_3170():
    assert subtract_3170(10, 4) == 6

def test_multiply_3171():
    assert multiply_3171(3, 7) == 21

def test_divide_3172():
    assert divide_3172(10, 2) == 5.0
