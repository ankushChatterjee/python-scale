"""Tests for test module 679 — covers src modules [2713, 2714, 2715, 2716]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2713 import add_2713
from module_2714 import subtract_2714
from module_2715 import multiply_2715
from module_2716 import divide_2716

def test_add_2713():
    assert add_2713(2, 3) == 5

def test_subtract_2714():
    assert subtract_2714(10, 4) == 6

def test_multiply_2715():
    assert multiply_2715(3, 7) == 21

def test_divide_2716():
    assert divide_2716(10, 2) == 5.0
