"""Tests for test module 659 — covers src modules [2633, 2634, 2635, 2636]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2633 import add_2633
from module_2634 import subtract_2634
from module_2635 import multiply_2635
from module_2636 import divide_2636

def test_add_2633():
    assert add_2633(2, 3) == 5

def test_subtract_2634():
    assert subtract_2634(10, 4) == 6

def test_multiply_2635():
    assert multiply_2635(3, 7) == 21

def test_divide_2636():
    assert divide_2636(10, 2) == 5.0
