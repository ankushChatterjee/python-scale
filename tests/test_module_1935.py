"""Tests for test module 1935 — covers src modules [7737, 7738, 7739, 7740]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7737 import add_7737
from module_7738 import subtract_7738
from module_7739 import multiply_7739
from module_7740 import divide_7740

def test_add_7737():
    assert add_7737(2, 3) == 5

def test_subtract_7738():
    assert subtract_7738(10, 4) == 6

def test_multiply_7739():
    assert multiply_7739(3, 7) == 21

def test_divide_7740():
    assert divide_7740(10, 2) == 5.0
