"""Tests for test module 1703 — covers src modules [6809, 6810, 6811, 6812]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6809 import add_6809
from module_6810 import subtract_6810
from module_6811 import multiply_6811
from module_6812 import divide_6812

def test_add_6809():
    assert add_6809(2, 3) == 5

def test_subtract_6810():
    assert subtract_6810(10, 4) == 6

def test_multiply_6811():
    assert multiply_6811(3, 7) == 21

def test_divide_6812():
    assert divide_6812(10, 2) == 5.0
