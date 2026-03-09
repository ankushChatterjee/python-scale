"""Tests for test module 691 — covers src modules [2761, 2762, 2763, 2764]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2761 import add_2761
from module_2762 import subtract_2762
from module_2763 import multiply_2763
from module_2764 import divide_2764

def test_add_2761():
    assert add_2761(2, 3) == 5

def test_subtract_2762():
    assert subtract_2762(10, 4) == 6

def test_multiply_2763():
    assert multiply_2763(3, 7) == 21

def test_divide_2764():
    assert divide_2764(10, 2) == 5.0
