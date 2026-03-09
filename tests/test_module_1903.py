"""Tests for test module 1903 — covers src modules [7609, 7610, 7611, 7612]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7609 import add_7609
from module_7610 import subtract_7610
from module_7611 import multiply_7611
from module_7612 import divide_7612

def test_add_7609():
    assert add_7609(2, 3) == 5

def test_subtract_7610():
    assert subtract_7610(10, 4) == 6

def test_multiply_7611():
    assert multiply_7611(3, 7) == 21

def test_divide_7612():
    assert divide_7612(10, 2) == 5.0
