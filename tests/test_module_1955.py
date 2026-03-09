"""Tests for test module 1955 — covers src modules [7817, 7818, 7819, 7820]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7817 import add_7817
from module_7818 import subtract_7818
from module_7819 import multiply_7819
from module_7820 import divide_7820

def test_add_7817():
    assert add_7817(2, 3) == 5

def test_subtract_7818():
    assert subtract_7818(10, 4) == 6

def test_multiply_7819():
    assert multiply_7819(3, 7) == 21

def test_divide_7820():
    assert divide_7820(10, 2) == 5.0
