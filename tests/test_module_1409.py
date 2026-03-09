"""Tests for test module 1409 — covers src modules [5633, 5634, 5635, 5636]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5633 import add_5633
from module_5634 import subtract_5634
from module_5635 import multiply_5635
from module_5636 import divide_5636

def test_add_5633():
    assert add_5633(2, 3) == 5

def test_subtract_5634():
    assert subtract_5634(10, 4) == 6

def test_multiply_5635():
    assert multiply_5635(3, 7) == 21

def test_divide_5636():
    assert divide_5636(10, 2) == 5.0
