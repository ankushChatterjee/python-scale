"""Tests for test module 2185 — covers src modules [8737, 8738, 8739, 8740]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8737 import add_8737
from module_8738 import subtract_8738
from module_8739 import multiply_8739
from module_8740 import divide_8740

def test_add_8737():
    assert add_8737(2, 3) == 5

def test_subtract_8738():
    assert subtract_8738(10, 4) == 6

def test_multiply_8739():
    assert multiply_8739(3, 7) == 21

def test_divide_8740():
    assert divide_8740(10, 2) == 5.0
