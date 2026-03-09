"""Tests for test module 1941 — covers src modules [7761, 7762, 7763, 7764]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7761 import add_7761
from module_7762 import subtract_7762
from module_7763 import multiply_7763
from module_7764 import divide_7764

def test_add_7761():
    assert add_7761(2, 3) == 5

def test_subtract_7762():
    assert subtract_7762(10, 4) == 6

def test_multiply_7763():
    assert multiply_7763(3, 7) == 21

def test_divide_7764():
    assert divide_7764(10, 2) == 5.0
