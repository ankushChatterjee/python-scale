"""Tests for test module 1697 — covers src modules [6785, 6786, 6787, 6788]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6785 import add_6785
from module_6786 import subtract_6786
from module_6787 import multiply_6787
from module_6788 import divide_6788

def test_add_6785():
    assert add_6785(2, 3) == 5

def test_subtract_6786():
    assert subtract_6786(10, 4) == 6

def test_multiply_6787():
    assert multiply_6787(3, 7) == 21

def test_divide_6788():
    assert divide_6788(10, 2) == 5.0
