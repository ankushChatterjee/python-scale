"""Tests for test module 1929 — covers src modules [7713, 7714, 7715, 7716]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7713 import add_7713
from module_7714 import subtract_7714
from module_7715 import multiply_7715
from module_7716 import divide_7716

def test_add_7713():
    assert add_7713(2, 3) == 5

def test_subtract_7714():
    assert subtract_7714(10, 4) == 6

def test_multiply_7715():
    assert multiply_7715(3, 7) == 21

def test_divide_7716():
    assert divide_7716(10, 2) == 5.0
