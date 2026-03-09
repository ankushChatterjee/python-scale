"""Tests for test module 1659 — covers src modules [6633, 6634, 6635, 6636]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6633 import add_6633
from module_6634 import subtract_6634
from module_6635 import multiply_6635
from module_6636 import divide_6636

def test_add_6633():
    assert add_6633(2, 3) == 5

def test_subtract_6634():
    assert subtract_6634(10, 4) == 6

def test_multiply_6635():
    assert multiply_6635(3, 7) == 21

def test_divide_6636():
    assert divide_6636(10, 2) == 5.0
