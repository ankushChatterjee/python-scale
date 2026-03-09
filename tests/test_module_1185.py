"""Tests for test module 1185 — covers src modules [4737, 4738, 4739, 4740]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4737 import add_4737
from module_4738 import subtract_4738
from module_4739 import multiply_4739
from module_4740 import divide_4740

def test_add_4737():
    assert add_4737(2, 3) == 5

def test_subtract_4738():
    assert subtract_4738(10, 4) == 6

def test_multiply_4739():
    assert multiply_4739(3, 7) == 21

def test_divide_4740():
    assert divide_4740(10, 2) == 5.0
