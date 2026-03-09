"""Tests for test module 459 — covers src modules [1833, 1834, 1835, 1836]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1833 import add_1833
from module_1834 import subtract_1834
from module_1835 import multiply_1835
from module_1836 import divide_1836

def test_add_1833():
    assert add_1833(2, 3) == 5

def test_subtract_1834():
    assert subtract_1834(10, 4) == 6

def test_multiply_1835():
    assert multiply_1835(3, 7) == 21

def test_divide_1836():
    assert divide_1836(10, 2) == 5.0
