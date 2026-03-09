"""Tests for test module 447 — covers src modules [1785, 1786, 1787, 1788]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1785 import add_1785
from module_1786 import subtract_1786
from module_1787 import multiply_1787
from module_1788 import divide_1788

def test_add_1785():
    assert add_1785(2, 3) == 5

def test_subtract_1786():
    assert subtract_1786(10, 4) == 6

def test_multiply_1787():
    assert multiply_1787(3, 7) == 21

def test_divide_1788():
    assert divide_1788(10, 2) == 5.0
