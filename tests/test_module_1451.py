"""Tests for test module 1451 — covers src modules [5801, 5802, 5803, 5804]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5801 import add_5801
from module_5802 import subtract_5802
from module_5803 import multiply_5803
from module_5804 import divide_5804

def test_add_5801():
    assert add_5801(2, 3) == 5

def test_subtract_5802():
    assert subtract_5802(10, 4) == 6

def test_multiply_5803():
    assert multiply_5803(3, 7) == 21

def test_divide_5804():
    assert divide_5804(10, 2) == 5.0
