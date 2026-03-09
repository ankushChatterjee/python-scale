"""Tests for test module 1793 — covers src modules [7169, 7170, 7171, 7172]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7169 import add_7169
from module_7170 import subtract_7170
from module_7171 import multiply_7171
from module_7172 import divide_7172

def test_add_7169():
    assert add_7169(2, 3) == 5

def test_subtract_7170():
    assert subtract_7170(10, 4) == 6

def test_multiply_7171():
    assert multiply_7171(3, 7) == 21

def test_divide_7172():
    assert divide_7172(10, 2) == 5.0
