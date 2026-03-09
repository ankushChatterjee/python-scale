"""Tests for test module 1403 — covers src modules [5609, 5610, 5611, 5612]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5609 import add_5609
from module_5610 import subtract_5610
from module_5611 import multiply_5611
from module_5612 import divide_5612

def test_add_5609():
    assert add_5609(2, 3) == 5

def test_subtract_5610():
    assert subtract_5610(10, 4) == 6

def test_multiply_5611():
    assert multiply_5611(3, 7) == 21

def test_divide_5612():
    assert divide_5612(10, 2) == 5.0
