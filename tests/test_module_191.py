"""Tests for test module 191 — covers src modules [761, 762, 763, 764]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_761 import add_761
from module_762 import subtract_762
from module_763 import multiply_763
from module_764 import divide_764

def test_add_761():
    assert add_761(2, 3) == 5

def test_subtract_762():
    assert subtract_762(10, 4) == 6

def test_multiply_763():
    assert multiply_763(3, 7) == 21

def test_divide_764():
    assert divide_764(10, 2) == 5.0
