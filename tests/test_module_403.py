"""Tests for test module 403 — covers src modules [1609, 1610, 1611, 1612]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1609 import add_1609
from module_1610 import subtract_1610
from module_1611 import multiply_1611
from module_1612 import divide_1612

def test_add_1609():
    assert add_1609(2, 3) == 5

def test_subtract_1610():
    assert subtract_1610(10, 4) == 6

def test_multiply_1611():
    assert multiply_1611(3, 7) == 21

def test_divide_1612():
    assert divide_1612(10, 2) == 5.0
