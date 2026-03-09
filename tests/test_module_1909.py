"""Tests for test module 1909 — covers src modules [7633, 7634, 7635, 7636]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7633 import add_7633
from module_7634 import subtract_7634
from module_7635 import multiply_7635
from module_7636 import divide_7636

def test_add_7633():
    assert add_7633(2, 3) == 5

def test_subtract_7634():
    assert subtract_7634(10, 4) == 6

def test_multiply_7635():
    assert multiply_7635(3, 7) == 21

def test_divide_7636():
    assert divide_7636(10, 2) == 5.0
