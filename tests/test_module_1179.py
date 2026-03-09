"""Tests for test module 1179 — covers src modules [4713, 4714, 4715, 4716]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4713 import add_4713
from module_4714 import subtract_4714
from module_4715 import multiply_4715
from module_4716 import divide_4716

def test_add_4713():
    assert add_4713(2, 3) == 5

def test_subtract_4714():
    assert subtract_4714(10, 4) == 6

def test_multiply_4715():
    assert multiply_4715(3, 7) == 21

def test_divide_4716():
    assert divide_4716(10, 2) == 5.0
