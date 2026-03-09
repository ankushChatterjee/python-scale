"""Tests for test module 1543 — covers src modules [6169, 6170, 6171, 6172]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6169 import add_6169
from module_6170 import subtract_6170
from module_6171 import multiply_6171
from module_6172 import divide_6172

def test_add_6169():
    assert add_6169(2, 3) == 5

def test_subtract_6170():
    assert subtract_6170(10, 4) == 6

def test_multiply_6171():
    assert multiply_6171(3, 7) == 21

def test_divide_6172():
    assert divide_6172(10, 2) == 5.0
