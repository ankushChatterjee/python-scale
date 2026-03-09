"""Tests for test module 685 — covers src modules [2737, 2738, 2739, 2740]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2737 import add_2737
from module_2738 import subtract_2738
from module_2739 import multiply_2739
from module_2740 import divide_2740

def test_add_2737():
    assert add_2737(2, 3) == 5

def test_subtract_2738():
    assert subtract_2738(10, 4) == 6

def test_multiply_2739():
    assert multiply_2739(3, 7) == 21

def test_divide_2740():
    assert divide_2740(10, 2) == 5.0
