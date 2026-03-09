"""Tests for test module 1429 — covers src modules [5713, 5714, 5715, 5716]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5713 import add_5713
from module_5714 import subtract_5714
from module_5715 import multiply_5715
from module_5716 import divide_5716

def test_add_5713():
    assert add_5713(2, 3) == 5

def test_subtract_5714():
    assert subtract_5714(10, 4) == 6

def test_multiply_5715():
    assert multiply_5715(3, 7) == 21

def test_divide_5716():
    assert divide_5716(10, 2) == 5.0
