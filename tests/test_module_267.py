"""Tests for test module 267 — covers src modules [1065, 1066, 1067, 1068]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1065 import add_1065
from module_1066 import subtract_1066
from module_1067 import multiply_1067
from module_1068 import divide_1068

def test_add_1065():
    assert add_1065(2, 3) == 5

def test_subtract_1066():
    assert subtract_1066(10, 4) == 6

def test_multiply_1067():
    assert multiply_1067(3, 7) == 21

def test_divide_1068():
    assert divide_1068(10, 2) == 5.0
