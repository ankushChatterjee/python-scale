"""Tests for test module 1685 — covers src modules [6737, 6738, 6739, 6740]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6737 import add_6737
from module_6738 import subtract_6738
from module_6739 import multiply_6739
from module_6740 import divide_6740

def test_add_6737():
    assert add_6737(2, 3) == 5

def test_subtract_6738():
    assert subtract_6738(10, 4) == 6

def test_multiply_6739():
    assert multiply_6739(3, 7) == 21

def test_divide_6740():
    assert divide_6740(10, 2) == 5.0
