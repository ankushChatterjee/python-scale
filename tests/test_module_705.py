"""Tests for test module 705 — covers src modules [2817, 2818, 2819, 2820]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2817 import add_2817
from module_2818 import subtract_2818
from module_2819 import multiply_2819
from module_2820 import divide_2820

def test_add_2817():
    assert add_2817(2, 3) == 5

def test_subtract_2818():
    assert subtract_2818(10, 4) == 6

def test_multiply_2819():
    assert multiply_2819(3, 7) == 21

def test_divide_2820():
    assert divide_2820(10, 2) == 5.0
