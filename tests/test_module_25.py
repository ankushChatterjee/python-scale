"""Tests for test module 25 — covers src modules [97, 98, 99, 100]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_97 import add_97
from module_98 import subtract_98
from module_99 import multiply_99
from module_100 import divide_100

def test_add_97():
    assert add_97(2, 3) == 5

def test_subtract_98():
    assert subtract_98(10, 4) == 6

def test_multiply_99():
    assert multiply_99(3, 7) == 21

def test_divide_100():
    assert divide_100(10, 2) == 5.0
