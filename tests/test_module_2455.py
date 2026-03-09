"""Tests for test module 2455 — covers src modules [9817, 9818, 9819, 9820]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9817 import add_9817
from module_9818 import subtract_9818
from module_9819 import multiply_9819
from module_9820 import divide_9820

def test_add_9817():
    assert add_9817(2, 3) == 5

def test_subtract_9818():
    assert subtract_9818(10, 4) == 6

def test_multiply_9819():
    assert multiply_9819(3, 7) == 21

def test_divide_9820():
    assert divide_9820(10, 2) == 5.0
