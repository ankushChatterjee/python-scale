"""Tests for test module 1739 — covers src modules [6953, 6954, 6955, 6956]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6953 import add_6953
from module_6954 import subtract_6954
from module_6955 import multiply_6955
from module_6956 import divide_6956

def test_add_6953():
    assert add_6953(2, 3) == 5

def test_subtract_6954():
    assert subtract_6954(10, 4) == 6

def test_multiply_6955():
    assert multiply_6955(3, 7) == 21

def test_divide_6956():
    assert divide_6956(10, 2) == 5.0
