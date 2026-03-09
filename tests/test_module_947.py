"""Tests for test module 947 — covers src modules [3785, 3786, 3787, 3788]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3785 import add_3785
from module_3786 import subtract_3786
from module_3787 import multiply_3787
from module_3788 import divide_3788

def test_add_3785():
    assert add_3785(2, 3) == 5

def test_subtract_3786():
    assert subtract_3786(10, 4) == 6

def test_multiply_3787():
    assert multiply_3787(3, 7) == 21

def test_divide_3788():
    assert divide_3788(10, 2) == 5.0
