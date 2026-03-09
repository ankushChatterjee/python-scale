"""Tests for test module 1455 — covers src modules [5817, 5818, 5819, 5820]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5817 import add_5817
from module_5818 import subtract_5818
from module_5819 import multiply_5819
from module_5820 import divide_5820

def test_add_5817():
    assert add_5817(2, 3) == 5

def test_subtract_5818():
    assert subtract_5818(10, 4) == 6

def test_multiply_5819():
    assert multiply_5819(3, 7) == 21

def test_divide_5820():
    assert divide_5820(10, 2) == 5.0
