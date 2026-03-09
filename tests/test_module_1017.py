"""Tests for test module 1017 — covers src modules [4065, 4066, 4067, 4068]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4065 import add_4065
from module_4066 import subtract_4066
from module_4067 import multiply_4067
from module_4068 import divide_4068

def test_add_4065():
    assert add_4065(2, 3) == 5

def test_subtract_4066():
    assert subtract_4066(10, 4) == 6

def test_multiply_4067():
    assert multiply_4067(3, 7) == 21

def test_divide_4068():
    assert divide_4068(10, 2) == 5.0
