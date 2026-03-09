"""Tests for test module 2179 — covers src modules [8713, 8714, 8715, 8716]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8713 import add_8713
from module_8714 import subtract_8714
from module_8715 import multiply_8715
from module_8716 import divide_8716

def test_add_8713():
    assert add_8713(2, 3) == 5

def test_subtract_8714():
    assert subtract_8714(10, 4) == 6

def test_multiply_8715():
    assert multiply_8715(3, 7) == 21

def test_divide_8716():
    assert divide_8716(10, 2) == 5.0
