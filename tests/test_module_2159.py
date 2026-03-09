"""Tests for test module 2159 — covers src modules [8633, 8634, 8635, 8636]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8633 import add_8633
from module_8634 import subtract_8634
from module_8635 import multiply_8635
from module_8636 import divide_8636

def test_add_8633():
    assert add_8633(2, 3) == 5

def test_subtract_8634():
    assert subtract_8634(10, 4) == 6

def test_multiply_8635():
    assert multiply_8635(3, 7) == 21

def test_divide_8636():
    assert divide_8636(10, 2) == 5.0
