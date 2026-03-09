"""Tests for test module 2409 — covers src modules [9633, 9634, 9635, 9636]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9633 import add_9633
from module_9634 import subtract_9634
from module_9635 import multiply_9635
from module_9636 import divide_9636

def test_add_9633():
    assert add_9633(2, 3) == 5

def test_subtract_9634():
    assert subtract_9634(10, 4) == 6

def test_multiply_9635():
    assert multiply_9635(3, 7) == 21

def test_divide_9636():
    assert divide_9636(10, 2) == 5.0
