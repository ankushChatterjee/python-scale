"""Tests for test module 1435 — covers src modules [5737, 5738, 5739, 5740]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5737 import add_5737
from module_5738 import subtract_5738
from module_5739 import multiply_5739
from module_5740 import divide_5740

def test_add_5737():
    assert add_5737(2, 3) == 5

def test_subtract_5738():
    assert subtract_5738(10, 4) == 6

def test_multiply_5739():
    assert multiply_5739(3, 7) == 21

def test_divide_5740():
    assert divide_5740(10, 2) == 5.0
