"""Tests for test module 1767 — covers src modules [7065, 7066, 7067, 7068]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7065 import add_7065
from module_7066 import subtract_7066
from module_7067 import multiply_7067
from module_7068 import divide_7068

def test_add_7065():
    assert add_7065(2, 3) == 5

def test_subtract_7066():
    assert subtract_7066(10, 4) == 6

def test_multiply_7067():
    assert multiply_7067(3, 7) == 21

def test_divide_7068():
    assert divide_7068(10, 2) == 5.0
