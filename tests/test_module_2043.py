"""Tests for test module 2043 — covers src modules [8169, 8170, 8171, 8172]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8169 import add_8169
from module_8170 import subtract_8170
from module_8171 import multiply_8171
from module_8172 import divide_8172

def test_add_8169():
    assert add_8169(2, 3) == 5

def test_subtract_8170():
    assert subtract_8170(10, 4) == 6

def test_multiply_8171():
    assert multiply_8171(3, 7) == 21

def test_divide_8172():
    assert divide_8172(10, 2) == 5.0
