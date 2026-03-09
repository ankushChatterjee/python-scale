"""Tests for test module 1293 — covers src modules [5169, 5170, 5171, 5172]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5169 import add_5169
from module_5170 import subtract_5170
from module_5171 import multiply_5171
from module_5172 import divide_5172

def test_add_5169():
    assert add_5169(2, 3) == 5

def test_subtract_5170():
    assert subtract_5170(10, 4) == 6

def test_multiply_5171():
    assert multiply_5171(3, 7) == 21

def test_divide_5172():
    assert divide_5172(10, 2) == 5.0
