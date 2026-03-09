"""Tests for test module 1947 — covers src modules [7785, 7786, 7787, 7788]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7785 import add_7785
from module_7786 import subtract_7786
from module_7787 import multiply_7787
from module_7788 import divide_7788

def test_add_7785():
    assert add_7785(2, 3) == 5

def test_subtract_7786():
    assert subtract_7786(10, 4) == 6

def test_multiply_7787():
    assert multiply_7787(3, 7) == 21

def test_divide_7788():
    assert divide_7788(10, 2) == 5.0
