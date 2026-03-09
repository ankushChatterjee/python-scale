"""Tests for test module 1267 — covers src modules [5065, 5066, 5067, 5068]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5065 import add_5065
from module_5066 import subtract_5066
from module_5067 import multiply_5067
from module_5068 import divide_5068

def test_add_5065():
    assert add_5065(2, 3) == 5

def test_subtract_5066():
    assert subtract_5066(10, 4) == 6

def test_multiply_5067():
    assert multiply_5067(3, 7) == 21

def test_divide_5068():
    assert divide_5068(10, 2) == 5.0
