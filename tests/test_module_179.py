"""Tests for test module 179 — covers src modules [713, 714, 715, 716]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_713 import add_713
from module_714 import subtract_714
from module_715 import multiply_715
from module_716 import divide_716

def test_add_713():
    assert add_713(2, 3) == 5

def test_subtract_714():
    assert subtract_714(10, 4) == 6

def test_multiply_715():
    assert multiply_715(3, 7) == 21

def test_divide_716():
    assert divide_716(10, 2) == 5.0
