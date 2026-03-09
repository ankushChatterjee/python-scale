"""Tests for test module 159 — covers src modules [633, 634, 635, 636]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_633 import add_633
from module_634 import subtract_634
from module_635 import multiply_635
from module_636 import divide_636

def test_add_633():
    assert add_633(2, 3) == 5

def test_subtract_634():
    assert subtract_634(10, 4) == 6

def test_multiply_635():
    assert multiply_635(3, 7) == 21

def test_divide_636():
    assert divide_636(10, 2) == 5.0
