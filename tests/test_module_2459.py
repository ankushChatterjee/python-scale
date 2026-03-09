"""Tests for test module 2459 — covers src modules [9833, 9834, 9835, 9836]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9833 import add_9833
from module_9834 import subtract_9834
from module_9835 import multiply_9835
from module_9836 import divide_9836

def test_add_9833():
    assert add_9833(2, 3) == 5

def test_subtract_9834():
    assert subtract_9834(10, 4) == 6

def test_multiply_9835():
    assert multiply_9835(3, 7) == 21

def test_divide_9836():
    assert divide_9836(10, 2) == 5.0
