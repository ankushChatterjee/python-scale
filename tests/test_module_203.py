"""Tests for test module 203 — covers src modules [809, 810, 811, 812]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_809 import add_809
from module_810 import subtract_810
from module_811 import multiply_811
from module_812 import divide_812

def test_add_809():
    assert add_809(2, 3) == 5

def test_subtract_810():
    assert subtract_810(10, 4) == 6

def test_multiply_811():
    assert multiply_811(3, 7) == 21

def test_divide_812():
    assert divide_812(10, 2) == 5.0
