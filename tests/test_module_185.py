"""Tests for test module 185 — covers src modules [737, 738, 739, 740]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_737 import add_737
from module_738 import subtract_738
from module_739 import multiply_739
from module_740 import divide_740

def test_add_737():
    assert add_737(2, 3) == 5

def test_subtract_738():
    assert subtract_738(10, 4) == 6

def test_multiply_739():
    assert multiply_739(3, 7) == 21

def test_divide_740():
    assert divide_740(10, 2) == 5.0
