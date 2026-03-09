"""Tests for test module 449 — covers src modules [1793, 1794, 1795, 1796]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1793 import add_1793
from module_1794 import subtract_1794
from module_1795 import multiply_1795
from module_1796 import divide_1796

def test_add_1793():
    assert add_1793(2, 3) == 5

def test_subtract_1794():
    assert subtract_1794(10, 4) == 6

def test_multiply_1795():
    assert multiply_1795(3, 7) == 21

def test_divide_1796():
    assert divide_1796(10, 2) == 5.0
