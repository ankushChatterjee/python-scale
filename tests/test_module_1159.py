"""Tests for test module 1159 — covers src modules [4633, 4634, 4635, 4636]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4633 import add_4633
from module_4634 import subtract_4634
from module_4635 import multiply_4635
from module_4636 import divide_4636

def test_add_4633():
    assert add_4633(2, 3) == 5

def test_subtract_4634():
    assert subtract_4634(10, 4) == 6

def test_multiply_4635():
    assert multiply_4635(3, 7) == 21

def test_divide_4636():
    assert divide_4636(10, 2) == 5.0
