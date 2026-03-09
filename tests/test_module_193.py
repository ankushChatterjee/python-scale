"""Tests for test module 193 — covers src modules [769, 770, 771, 772]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_769 import add_769
from module_770 import subtract_770
from module_771 import multiply_771
from module_772 import divide_772

def test_add_769():
    assert add_769(2, 3) == 5

def test_subtract_770():
    assert subtract_770(10, 4) == 6

def test_multiply_771():
    assert multiply_771(3, 7) == 21

def test_divide_772():
    assert divide_772(10, 2) == 5.0
