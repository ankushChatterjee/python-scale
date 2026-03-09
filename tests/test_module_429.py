"""Tests for test module 429 — covers src modules [1713, 1714, 1715, 1716]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1713 import add_1713
from module_1714 import subtract_1714
from module_1715 import multiply_1715
from module_1716 import divide_1716

def test_add_1713():
    assert add_1713(2, 3) == 5

def test_subtract_1714():
    assert subtract_1714(10, 4) == 6

def test_multiply_1715():
    assert multiply_1715(3, 7) == 21

def test_divide_1716():
    assert divide_1716(10, 2) == 5.0
