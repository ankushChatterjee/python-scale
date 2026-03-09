"""Tests for test module 443 — covers src modules [1769, 1770, 1771, 1772]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1769 import add_1769
from module_1770 import subtract_1770
from module_1771 import multiply_1771
from module_1772 import divide_1772

def test_add_1769():
    assert add_1769(2, 3) == 5

def test_subtract_1770():
    assert subtract_1770(10, 4) == 6

def test_multiply_1771():
    assert multiply_1771(3, 7) == 21

def test_divide_1772():
    assert divide_1772(10, 2) == 5.0
