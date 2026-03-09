"""Tests for test module 43 — covers src modules [169, 170, 171, 172]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_169 import add_169
from module_170 import subtract_170
from module_171 import multiply_171
from module_172 import divide_172

def test_add_169():
    assert add_169(2, 3) == 5

def test_subtract_170():
    assert subtract_170(10, 4) == 6

def test_multiply_171():
    assert multiply_171(3, 7) == 21

def test_divide_172():
    assert divide_172(10, 2) == 5.0
