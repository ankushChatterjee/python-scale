"""Tests for test module 2435 — covers src modules [9737, 9738, 9739, 9740]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9737 import add_9737
from module_9738 import subtract_9738
from module_9739 import multiply_9739
from module_9740 import divide_9740

def test_add_9737():
    assert add_9737(2, 3) == 5

def test_subtract_9738():
    assert subtract_9738(10, 4) == 6

def test_multiply_9739():
    assert multiply_9739(3, 7) == 21

def test_divide_9740():
    assert divide_9740(10, 2) == 5.0
