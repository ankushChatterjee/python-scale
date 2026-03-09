"""Tests for test module 423 — covers src modules [1689, 1690, 1691, 1692]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1689 import add_1689
from module_1690 import subtract_1690
from module_1691 import multiply_1691
from module_1692 import divide_1692

def test_add_1689():
    assert add_1689(2, 3) == 5

def test_subtract_1690():
    assert subtract_1690(10, 4) == 6

def test_multiply_1691():
    assert multiply_1691(3, 7) == 21

def test_divide_1692():
    assert divide_1692(10, 2) == 5.0
