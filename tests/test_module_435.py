"""Tests for test module 435 — covers src modules [1737, 1738, 1739, 1740]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1737 import add_1737
from module_1738 import subtract_1738
from module_1739 import multiply_1739
from module_1740 import divide_1740

def test_add_1737():
    assert add_1737(2, 3) == 5

def test_subtract_1738():
    assert subtract_1738(10, 4) == 6

def test_multiply_1739():
    assert multiply_1739(3, 7) == 21

def test_divide_1740():
    assert divide_1740(10, 2) == 5.0
