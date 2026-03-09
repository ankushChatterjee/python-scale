"""Tests for test module 1205 — covers src modules [4817, 4818, 4819, 4820]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4817 import add_4817
from module_4818 import subtract_4818
from module_4819 import multiply_4819
from module_4820 import divide_4820

def test_add_4817():
    assert add_4817(2, 3) == 5

def test_subtract_4818():
    assert subtract_4818(10, 4) == 6

def test_multiply_4819():
    assert multiply_4819(3, 7) == 21

def test_divide_4820():
    assert divide_4820(10, 2) == 5.0
