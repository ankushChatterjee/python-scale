"""Tests for test module 2267 — covers src modules [9065, 9066, 9067, 9068]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9065 import add_9065
from module_9066 import subtract_9066
from module_9067 import multiply_9067
from module_9068 import divide_9068

def test_add_9065():
    assert add_9065(2, 3) == 5

def test_subtract_9066():
    assert subtract_9066(10, 4) == 6

def test_multiply_9067():
    assert multiply_9067(3, 7) == 21

def test_divide_9068():
    assert divide_9068(10, 2) == 5.0
