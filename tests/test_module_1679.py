"""Tests for test module 1679 — covers src modules [6713, 6714, 6715, 6716]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6713 import add_6713
from module_6714 import subtract_6714
from module_6715 import multiply_6715
from module_6716 import divide_6716

def test_add_6713():
    assert add_6713(2, 3) == 5

def test_subtract_6714():
    assert subtract_6714(10, 4) == 6

def test_multiply_6715():
    assert multiply_6715(3, 7) == 21

def test_divide_6716():
    assert divide_6716(10, 2) == 5.0
