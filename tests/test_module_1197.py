"""Tests for test module 1197 — covers src modules [4785, 4786, 4787, 4788]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4785 import add_4785
from module_4786 import subtract_4786
from module_4787 import multiply_4787
from module_4788 import divide_4788

def test_add_4785():
    assert add_4785(2, 3) == 5

def test_subtract_4786():
    assert subtract_4786(10, 4) == 6

def test_multiply_4787():
    assert multiply_4787(3, 7) == 21

def test_divide_4788():
    assert divide_4788(10, 2) == 5.0
