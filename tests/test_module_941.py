"""Tests for test module 941 — covers src modules [3761, 3762, 3763, 3764]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3761 import add_3761
from module_3762 import subtract_3762
from module_3763 import multiply_3763
from module_3764 import divide_3764

def test_add_3761():
    assert add_3761(2, 3) == 5

def test_subtract_3762():
    assert subtract_3762(10, 4) == 6

def test_multiply_3763():
    assert multiply_3763(3, 7) == 21

def test_divide_3764():
    assert divide_3764(10, 2) == 5.0
