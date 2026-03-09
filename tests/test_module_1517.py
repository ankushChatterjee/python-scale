"""Tests for test module 1517 — covers src modules [6065, 6066, 6067, 6068]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6065 import add_6065
from module_6066 import subtract_6066
from module_6067 import multiply_6067
from module_6068 import divide_6068

def test_add_6065():
    assert add_6065(2, 3) == 5

def test_subtract_6066():
    assert subtract_6066(10, 4) == 6

def test_multiply_6067():
    assert multiply_6067(3, 7) == 21

def test_divide_6068():
    assert divide_6068(10, 2) == 5.0
