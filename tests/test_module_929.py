"""Tests for test module 929 — covers src modules [3713, 3714, 3715, 3716]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3713 import add_3713
from module_3714 import subtract_3714
from module_3715 import multiply_3715
from module_3716 import divide_3716

def test_add_3713():
    assert add_3713(2, 3) == 5

def test_subtract_3714():
    assert subtract_3714(10, 4) == 6

def test_multiply_3715():
    assert multiply_3715(3, 7) == 21

def test_divide_3716():
    assert divide_3716(10, 2) == 5.0
