"""Tests for test module 453 — covers src modules [1809, 1810, 1811, 1812]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1809 import add_1809
from module_1810 import subtract_1810
from module_1811 import multiply_1811
from module_1812 import divide_1812

def test_add_1809():
    assert add_1809(2, 3) == 5

def test_subtract_1810():
    assert subtract_1810(10, 4) == 6

def test_multiply_1811():
    assert multiply_1811(3, 7) == 21

def test_divide_1812():
    assert divide_1812(10, 2) == 5.0
