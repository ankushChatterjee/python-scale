"""Tests for test module 909 — covers src modules [3633, 3634, 3635, 3636]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3633 import add_3633
from module_3634 import subtract_3634
from module_3635 import multiply_3635
from module_3636 import divide_3636

def test_add_3633():
    assert add_3633(2, 3) == 5

def test_subtract_3634():
    assert subtract_3634(10, 4) == 6

def test_multiply_3635():
    assert multiply_3635(3, 7) == 21

def test_divide_3636():
    assert divide_3636(10, 2) == 5.0
