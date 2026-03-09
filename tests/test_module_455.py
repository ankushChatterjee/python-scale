"""Tests for test module 455 — covers src modules [1817, 1818, 1819, 1820]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1817 import add_1817
from module_1818 import subtract_1818
from module_1819 import multiply_1819
from module_1820 import divide_1820

def test_add_1817():
    assert add_1817(2, 3) == 5

def test_subtract_1818():
    assert subtract_1818(10, 4) == 6

def test_multiply_1819():
    assert multiply_1819(3, 7) == 21

def test_divide_1820():
    assert divide_1820(10, 2) == 5.0
