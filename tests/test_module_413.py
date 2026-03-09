"""Tests for test module 413 — covers src modules [1649, 1650, 1651, 1652]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1649 import add_1649
from module_1650 import subtract_1650
from module_1651 import multiply_1651
from module_1652 import divide_1652

def test_add_1649():
    assert add_1649(2, 3) == 5

def test_subtract_1650():
    assert subtract_1650(10, 4) == 6

def test_multiply_1651():
    assert multiply_1651(3, 7) == 21

def test_divide_1652():
    assert divide_1652(10, 2) == 5.0
