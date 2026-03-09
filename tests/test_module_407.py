"""Tests for test module 407 — covers src modules [1625, 1626, 1627, 1628]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1625 import add_1625
from module_1626 import subtract_1626
from module_1627 import multiply_1627
from module_1628 import divide_1628

def test_add_1625():
    assert add_1625(2, 3) == 5

def test_subtract_1626():
    assert subtract_1626(10, 4) == 6

def test_multiply_1627():
    assert multiply_1627(3, 7) == 21

def test_divide_1628():
    assert divide_1628(10, 2) == 5.0
